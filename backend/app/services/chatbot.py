import asyncio
import json
import time
import uuid
from datetime import datetime
from typing import Dict, List, Optional, Any, Tuple
import openai
from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from sqlalchemy.orm import selectinload

from app.core.config import get_settings
from app.db.models import Conversation, ChatMessage, ChatbotAnalytics, KnowledgeBase, User
from app.schemas.chatbot import (
    ChatRequest, ChatResponse, ConversationCreate, ConversationResponse,
    Message, MessageRole, Language, ChatbotFeedback
)

settings = get_settings()

# Configure OpenAI client
openai.api_key = settings.OPENAI_API_KEY


class ChatbotService:
    def __init__(self):
        self.system_prompts = {
            Language.ENGLISH: """You are Kipesa, a helpful AI financial assistant for Tanzanian users. 
            You provide personalized financial advice, help with budgeting, explain Tanzanian financial regulations, 
            and assist with financial planning. Be conversational, empathetic, and culturally aware. 
            Always provide practical, actionable advice. If you're unsure about specific regulations, 
            recommend consulting official sources like Bank of Tanzania or TRA.""",
            
            Language.SWAHILI: """Wewe ni Kipesa, msaidizi wa AI wa kifedha kwa watumiaji wa Tanzania. 
            Unatoa ushauri wa kifedha wa kibinafsi, kusaidia na bajeti, kuelezea kanuni za kifedha za Tanzania, 
            na kusaidia na mpango wa kifedha. Kuwa mwenye mazungumzo, mwenye huruma, na mwenye ufahamu wa kitamaduni. 
            Daima toa ushauri wa vitendo, unaoweza kutekelezwa. Ikiwa huna uhakika kuhusu kanuni maalum, 
            pendekeza kushauriana na vyanzo rasmi kama Benki ya Tanzania au TRA."""
        }
        
        self.knowledge_base_cache = {}
        self.cache_ttl = 3600  # 1 hour

    async def create_conversation(
        self, 
        db: AsyncSession, 
        conversation_data: ConversationCreate,
        user_id: Optional[int] = None
    ) -> ConversationResponse:
        """Create a new conversation."""
        try:
            # Create conversation
            conversation = Conversation(
                id=str(uuid.uuid4()),
                user_id=user_id,
                language=conversation_data.language.value,
                meta_data=conversation_data.context
            )
            db.add(conversation)
            await db.commit()
            await db.refresh(conversation)
            
            # Add initial system message
            system_message = ChatMessage(
                id=str(uuid.uuid4()),
                conversation_id=conversation.id,
                role=MessageRole.SYSTEM.value,
                content=self.system_prompts[conversation_data.language]
            )
            db.add(system_message)
            
            # Add user's initial message
            user_message = ChatMessage(
                id=str(uuid.uuid4()),
                conversation_id=conversation.id,
                role=MessageRole.USER.value,
                content=conversation_data.initial_message
            )
            db.add(user_message)
            
            await db.commit()
            
            # Generate response
            response = await self._generate_response(
                db, conversation.id, conversation_data.initial_message, 
                conversation_data.language, user_id
            )
            
            return ConversationResponse(
                conversation_id=conversation.id,
                messages=[
                    Message(
                        role=MessageRole.SYSTEM,
                        content=system_message.content,
                        timestamp=system_message.timestamp
                    ),
                    Message(
                        role=MessageRole.USER,
                        content=user_message.content,
                        timestamp=user_message.timestamp
                    ),
                    Message(
                        role=MessageRole.ASSISTANT,
                        content=response.message,
                        timestamp=datetime.utcnow()
                    )
                ],
                language=conversation_data.language,
                created_at=conversation.created_at,
                updated_at=conversation.updated_at,
                user_id=user_id,
                metadata=conversation.meta_data
            )
            
        except Exception as e:
            logger.error(f"Error creating conversation: {e}")
            await db.rollback()
            raise

    async def process_message(
        self, 
        db: AsyncSession, 
        chat_request: ChatRequest,
        user_id: Optional[int] = None
    ) -> ChatResponse:
        """Process a user message and generate a response."""
        start_time = time.time()
        
        try:
            # Get or create conversation
            conversation_id = chat_request.conversation_id
            if not conversation_id:
                # Create new conversation
                conversation = Conversation(
                    id=str(uuid.uuid4()),
                    user_id=user_id,
                    language=chat_request.language.value,
                    meta_data=chat_request.context
                )
                db.add(conversation)
                await db.commit()
                await db.refresh(conversation)
                conversation_id = conversation.id
                
                # Add system message
                system_message = ChatMessage(
                    id=str(uuid.uuid4()),
                    conversation_id=conversation_id,
                    role=MessageRole.SYSTEM.value,
                    content=self.system_prompts[chat_request.language]
                )
                db.add(system_message)
            
            # Add user message
            user_message = ChatMessage(
                id=str(uuid.uuid4()),
                conversation_id=conversation_id,
                role=MessageRole.USER.value,
                content=chat_request.message
            )
            db.add(user_message)
            await db.commit()
            
            # Generate response
            response = await self._generate_response(
                db, conversation_id, chat_request.message, 
                chat_request.language, user_id
            )
            
            response_time = time.time() - start_time
            
            return ChatResponse(
                conversation_id=conversation_id,
                message=response.message,
                language=chat_request.language,
                confidence=response.confidence,
                intent=response.intent,
                entities=response.entities,
                sentiment=response.sentiment,
                response_time=response_time,
                metadata=response.metadata
            )
            
        except Exception as e:
            logger.error(f"Error processing message: {e}")
            await db.rollback()
            raise

    async def _generate_response(
        self, 
        db: AsyncSession, 
        conversation_id: str, 
        user_message: str,
        language: Language,
        user_id: Optional[int] = None
    ) -> ChatResponse:
        """Generate response using OpenAI API with context and knowledge base."""
        try:
            # Get conversation history
            messages = await self._get_conversation_history(db, conversation_id)
            
            # Get relevant knowledge base content
            knowledge_content = await self._get_relevant_knowledge(
                db, user_message, language
            )
            
            # Prepare messages for OpenAI
            openai_messages = []
            
            # Add system message with knowledge base context
            system_content = self.system_prompts[language]
            if knowledge_content:
                system_content += f"\n\nRelevant information:\n{knowledge_content}"
            
            openai_messages.append({
                "role": "system",
                "content": system_content
            })
            
            # Add conversation history (limit to last 10 messages for context)
            for msg in messages[-10:]:
                openai_messages.append({
                    "role": msg.role,
                    "content": msg.content
                })
            
            # Add user's current message
            openai_messages.append({
                "role": "user",
                "content": user_message
            })
            
            # Get user profile for personalization
            user_profile = None
            if user_id:
                user_profile = await self._get_user_profile(db, user_id)
            
            # Add user context if available
            if user_profile:
                context_message = f"User profile: {user_profile['age_group']}, {user_profile['location']}, {user_profile['language']}"
                openai_messages.append({
                    "role": "system",
                    "content": context_message
                })
            
            # Call OpenAI API
            client = openai.AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
            response = await client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=openai_messages,
                max_tokens=500,
                temperature=0.7,
                presence_penalty=0.1,
                frequency_penalty=0.1
            )
            
            assistant_message = response.choices[0].message.content
            
            # Save assistant message
            assistant_msg = ChatMessage(
                id=str(uuid.uuid4()),
                conversation_id=conversation_id,
                role=MessageRole.ASSISTANT.value,
                content=assistant_message
            )
            db.add(assistant_msg)
            await db.commit()
            
            # Analyze response for analytics
            analytics = await self._analyze_response(
                db, conversation_id, assistant_msg.id, 
                user_message, assistant_message, language
            )
            
            return ChatResponse(
                conversation_id=conversation_id,
                message=assistant_message,
                language=language,
                confidence=analytics.get('confidence', 0.8),
                intent=analytics.get('intent'),
                entities=analytics.get('entities'),
                sentiment=analytics.get('sentiment'),
                response_time=0.0,  # Will be set by caller
                metadata={
                    'knowledge_used': bool(knowledge_content),
                    'user_profile_used': bool(user_profile)
                }
            )
            
        except Exception as e:
            logger.error(f"Error generating response: {e}")
            raise

    async def _get_conversation_history(
        self, 
        db: AsyncSession, 
        conversation_id: str
    ) -> List[ChatMessage]:
        """Get conversation history."""
        query = select(ChatMessage).where(
            ChatMessage.conversation_id == conversation_id
        ).order_by(ChatMessage.timestamp)
        
        result = await db.execute(query)
        return result.scalars().all()

    async def _get_relevant_knowledge(
        self, 
        db: AsyncSession, 
        user_message: str, 
        language: Language
    ) -> Optional[str]:
        """Get relevant knowledge base content."""
        try:
            # Simple keyword matching for now
            # In production, you'd use semantic search or embeddings
            keywords = user_message.lower().split()
            
            query = select(KnowledgeBase).where(
                KnowledgeBase.language == language.value,
                KnowledgeBase.is_active == True
            )
            
            result = await db.execute(query)
            knowledge_items = result.scalars().all()
            
            relevant_content = []
            for item in knowledge_items:
                content_lower = item.content.lower()
                title_lower = item.title.lower()
                
                # Check if any keywords match
                for keyword in keywords:
                    if keyword in content_lower or keyword in title_lower:
                        relevant_content.append(f"{item.title}: {item.content}")
                        break
            
            return "\n\n".join(relevant_content[:3]) if relevant_content else None
            
        except Exception as e:
            logger.error(f"Error getting knowledge: {e}")
            return None

    async def _get_user_profile(
        self, 
        db: AsyncSession, 
        user_id: int
    ) -> Optional[Dict[str, Any]]:
        """Get user profile for personalization."""
        try:
            query = select(User).where(User.id == user_id)
            result = await db.execute(query)
            user = result.scalar_one_or_none()
            
            if user:
                return {
                    'age_group': user.age_group,
                    'location': user.location,
                    'language': user.language
                }
            return None
            
        except Exception as e:
            logger.error(f"Error getting user profile: {e}")
            return None

    async def _analyze_response(
        self, 
        db: AsyncSession, 
        conversation_id: str, 
        message_id: str,
        user_message: str, 
        assistant_message: str,
        language: Language
    ) -> Dict[str, Any]:
        """Analyze response for intent, entities, and sentiment."""
        try:
            # Simple analysis for now
            # In production, you'd use NLP libraries or AI services
            
            # Intent classification
            intent = self._classify_intent(user_message.lower())
            
            # Entity extraction
            entities = self._extract_entities(user_message)
            
            # Sentiment analysis
            sentiment = self._analyze_sentiment(assistant_message)
            
            # Save analytics
            analytics = ChatbotAnalytics(
                id=str(uuid.uuid4()),
                conversation_id=conversation_id,
                message_id=message_id,
                intent=intent,
                confidence=0.8,  # Default confidence
                entities=entities,
                sentiment=sentiment,
                response_time=0.0
            )
            db.add(analytics)
            await db.commit()
            
            return {
                'intent': intent,
                'entities': entities,
                'sentiment': sentiment,
                'confidence': 0.8
            }
            
        except Exception as e:
            logger.error(f"Error analyzing response: {e}")
            return {}

    def _classify_intent(self, message: str) -> str:
        """Classify user intent."""
        message = message.lower()
        
        if any(word in message for word in ['budget', 'bajeti', 'spending', 'expense']):
            return 'budget_help'
        elif any(word in message for word in ['save', 'saving', 'investment', 'wekeza']):
            return 'savings_advice'
        elif any(word in message for word in ['loan', 'mikopo', 'credit', 'debt']):
            return 'loan_advice'
        elif any(word in message for word in ['tax', 'kodi', 'tra', 'vat']):
            return 'tax_help'
        elif any(word in message for word in ['regulation', 'kanuni', 'policy']):
            return 'regulation_info'
        elif any(word in message for word in ['hello', 'hi', 'jambo', 'habari']):
            return 'greeting'
        else:
            return 'general_help'

    def _extract_entities(self, message: str) -> List[Dict[str, Any]]:
        """Extract entities from message."""
        entities = []
        message_lower = message.lower()
        
        # Extract amounts
        import re
        amount_pattern = r'(\d+(?:,\d+)*(?:\.\d+)?)\s*(?:tsh|shilling|dollar|euro|pound)'
        amounts = re.findall(amount_pattern, message_lower)
        for amount in amounts:
            entities.append({
                'type': 'amount',
                'value': amount,
                'currency': 'TSh'
            })
        
        # Extract time periods
        time_words = ['month', 'year', 'week', 'mwezi', 'mwaka', 'wiki']
        for word in time_words:
            if word in message_lower:
                entities.append({
                    'type': 'time_period',
                    'value': word
                })
        
        return entities

    def _analyze_sentiment(self, message: str) -> str:
        """Analyze sentiment of assistant response."""
        positive_words = ['good', 'great', 'excellent', 'helpful', 'positive', 'nzuri', 'mzuri']
        negative_words = ['bad', 'poor', 'negative', 'problem', 'mbaya', 'tatizo']
        
        message_lower = message.lower()
        
        positive_count = sum(1 for word in positive_words if word in message_lower)
        negative_count = sum(1 for word in negative_words if word in message_lower)
        
        if positive_count > negative_count:
            return 'positive'
        elif negative_count > positive_count:
            return 'negative'
        else:
            return 'neutral'

    async def get_conversation_history(
        self, 
        db: AsyncSession, 
        conversation_id: str
    ) -> Optional[ConversationResponse]:
        """Get conversation history."""
        try:
            # Get conversation
            query = select(Conversation).where(Conversation.id == conversation_id)
            result = await db.execute(query)
            conversation = result.scalar_one_or_none()
            
            if not conversation:
                return None
            
            # Get messages
            messages_query = select(ChatMessage).where(
                ChatMessage.conversation_id == conversation_id
            ).order_by(ChatMessage.timestamp)
            
            messages_result = await db.execute(messages_query)
            messages = messages_result.scalars().all()
            
            return ConversationResponse(
                conversation_id=conversation.id,
                messages=[
                    Message(
                        role=MessageRole(msg.role),
                        content=msg.content,
                        timestamp=msg.timestamp,
                        metadata=msg.meta_data
                    ) for msg in messages
                ],
                language=Language(conversation.language),
                created_at=conversation.created_at,
                updated_at=conversation.updated_at,
                user_id=conversation.user_id,
                metadata=conversation.meta_data
            )
            
        except Exception as e:
            logger.error(f"Error getting conversation history: {e}")
            return None

    async def submit_feedback(
        self, 
        db: AsyncSession, 
        feedback_data: ChatbotFeedback
    ) -> bool:
        """Submit feedback for a chatbot response."""
        try:
            feedback = ChatbotFeedback(
                id=str(uuid.uuid4()),
                conversation_id=feedback_data.conversation_id,
                message_id=feedback_data.message_id,
                rating=feedback_data.rating,
                feedback=feedback_data.feedback,
                helpful=feedback_data.helpful
            )
            
            db.add(feedback)
            await db.commit()
            
            return True
            
        except Exception as e:
            logger.error(f"Error submitting feedback: {e}")
            await db.rollback()
            return False

    async def get_analytics(
        self, 
        db: AsyncSession,
        user_id: Optional[int] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None
    ) -> Dict[str, Any]:
        """Get chatbot analytics."""
        try:
            # Get basic stats
            conversations_query = select(Conversation)
            if user_id:
                conversations_query = conversations_query.where(Conversation.user_id == user_id)
            if start_date:
                conversations_query = conversations_query.where(Conversation.created_at >= start_date)
            if end_date:
                conversations_query = conversations_query.where(Conversation.created_at <= end_date)
            
            result = await db.execute(conversations_query)
            conversations = result.scalars().all()
            
            total_conversations = len(conversations)
            
            # Get total messages
            messages_query = select(ChatMessage)
            if user_id:
                messages_query = messages_query.join(Conversation).where(Conversation.user_id == user_id)
            
            messages_result = await db.execute(messages_query)
            total_messages = len(messages_result.scalars().all())
            
            # Get average response time
            analytics_query = select(ChatbotAnalytics.response_time)
            if user_id:
                analytics_query = analytics_query.join(Conversation).where(Conversation.user_id == user_id)
            
            analytics_result = await db.execute(analytics_query)
            response_times = [rt for rt in analytics_result.scalars().all() if rt is not None]
            avg_response_time = sum(response_times) / len(response_times) if response_times else 0
            
            # Get language distribution
            language_distribution = {}
            for conv in conversations:
                lang = conv.language
                language_distribution[lang] = language_distribution.get(lang, 0) + 1
            
            # Get top intents
            intent_query = select(ChatbotAnalytics.intent, ChatbotAnalytics.confidence)
            if user_id:
                intent_query = intent_query.join(Conversation).where(Conversation.user_id == user_id)
            
            intent_result = await db.execute(intent_query)
            intents = intent_result.all()
            
            intent_counts = {}
            for intent, confidence in intents:
                if intent:
                    intent_counts[intent] = intent_counts.get(intent, 0) + 1
            
            top_intents = [
                {'intent': intent, 'count': count}
                for intent, count in sorted(intent_counts.items(), key=lambda x: x[1], reverse=True)[:5]
            ]
            
            return {
                'total_conversations': total_conversations,
                'total_messages': total_messages,
                'average_response_time': avg_response_time,
                'average_confidence': 0.8,  # Default for now
                'language_distribution': language_distribution,
                'top_intents': top_intents,
                'sentiment_distribution': {'positive': 0, 'negative': 0, 'neutral': 0}  # Placeholder
            }
            
        except Exception as e:
            logger.error(f"Error getting analytics: {e}")
            return {}


# Create service instance
chatbot_service = ChatbotService() 