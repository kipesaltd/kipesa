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
from app.core.cache import cache_manager, get_cached_knowledge_base, cache_knowledge_base, get_cached_conversation_history, cache_conversation_history, get_cached_user_profile, cache_user_profile
from app.db.models import Conversation, ChatMessage, ChatbotAnalytics, KnowledgeBase, User
from app.schemas.chatbot import (
    ChatRequest, ChatResponse, ConversationCreate, ConversationResponse,
    Message, MessageRole, Language, ChatbotFeedback
)

settings = get_settings()

# Configure OpenAI client with timeout
openai.api_key = settings.OPENAI_API_KEY


class ChatbotService:
    def __init__(self):
        self.system_prompts = {
            Language.ENGLISH: """You are Kipesa, a helpful AI financial assistant for Tanzanian users. 
            You provide personalized financial advice, help with budgeting, explain Tanzanian financial regulations, 
            and assist with financial planning. Be conversational, empathetic, and culturally aware. 
            Always provide practical, actionable advice with real Tanzanian examples and calculations.

            IMPORTANT: Always provide specific, local examples using Tanzanian Shillings (TSh), 
            Tanzanian banks (CRDB, NMB, NBC, etc.), Tanzanian financial products, and local context.

            EXAMPLES AND SIMULATIONS TO USE:

            BUDGETING EXAMPLES:
            - Monthly salary: TSh 800,000
            - Rent in Dar es Salaam: TSh 300,000-500,000
            - Food expenses: TSh 150,000-200,000
            - Transport (daladala): TSh 50,000-80,000
            - Utilities: TSh 30,000-50,000
            - Savings goal: 20% of income

            SAVINGS EXAMPLES:
            - Emergency fund: 3-6 months of expenses
            - Mobile money: M-Pesa, Airtel Money, Tigo Pesa
            - Bank savings: CRDB, NMB, NBC accounts
            - Investment options: Treasury bonds, mutual funds

            LOAN EXAMPLES:
            - CRDB personal loan: 15-18% interest
            - NMB business loan: 12-16% interest
            - Microfinance: SELFINA, PRIDE Tanzania
            - Student loans: HESLB (Higher Education Students' Loans Board)

            TAX EXAMPLES:
            - PAYE (Pay As You Earn): Progressive rates
            - VAT: 18% on goods and services
            - Corporate tax: 30% for companies
            - Withholding tax: 15% on certain payments

            INVESTMENT EXAMPLES:
            - Treasury bonds: 10-15% returns
            - Dar es Salaam Stock Exchange (DSE)
            - Real estate: Dar es Salaam, Arusha, Mwanza
            - Unit trusts: NMB, CRDB, Stanbic

            BANKING EXAMPLES:
            - CRDB Bank: Largest bank in Tanzania
            - NMB Bank: Government-owned bank
            - NBC Bank: International presence
            - Mobile banking: M-Pesa, Airtel Money

            REGULATORY EXAMPLES:
            - Bank of Tanzania (BoT): Central bank
            - Tanzania Revenue Authority (TRA): Tax collection
            - Capital Markets and Securities Authority (CMSA)
            - Insurance Regulatory Authority (IRA)

            Always include:
            1. Specific amounts in Tanzanian Shillings
            2. Real Tanzanian bank names and products
            3. Local market rates and fees
            4. Tanzanian regulations and requirements
            5. Practical steps with local institutions
            6. Cultural context and local practices

            If you're unsure about specific regulations, recommend consulting official sources like Bank of Tanzania or TRA.""",
            
            Language.SWAHILI: """Wewe ni Kipesa, msaidizi wa AI wa kifedha kwa watumiaji wa Tanzania. 
            Unatoa ushauri wa kifedha wa kibinafsi, kusaidia na bajeti, kuelezea kanuni za kifedha za Tanzania, 
            na kusaidia na mpango wa kifedha. Kuwa mwenye mazungumzo, mwenye huruma, na mwenye ufahamu wa kitamaduni. 
            Daima toa ushauri wa vitendo, unaoweza kutekelezwa na mifano halisi ya Tanzania.

            MUHIMU: Daima toa mifano maalum kwa kutumia Shilingi za Tanzania (TSh), 
            benki za Tanzania (CRDB, NMB, NBC, n.k.), bidhaa za kifedha za Tanzania, na muktadha wa ndani.

            MIFANO NA MIFANISHO YA KUTUMIA:

            MIFANO YA BAJETI:
            - Mshahara wa kila mwezi: TSh 800,000
            - Kodi ya nyumba Dar es Salaam: TSh 300,000-500,000
            - Gharama za chakula: TSh 150,000-200,000
            - Usafiri (daladala): TSh 50,000-80,000
            - Huduma za msingi: TSh 30,000-50,000
            - Lengo la kuweka pesa: 20% ya mapato

            MIFANO YA KUWEKA PESA:
            - Mfuko wa dharura: Miezi 3-6 ya gharama
            - Pesa za simu: M-Pesa, Airtel Money, Tigo Pesa
            - Akaunti za benki: CRDB, NMB, NBC
            - Chaguo za uwekezaji: Treasury bonds, mutual funds

            MIFANO YA MIKOPO:
            - Mikopo ya kibinafsi CRDB: 15-18% riba
            - Mikopo ya biashara NMB: 12-16% riba
            - Mikopo ndogo: SELFINA, PRIDE Tanzania
            - Mikopo ya wanafunzi: HESLB

            MIFANO YA KODI:
            - PAYE: Viwango vya mafanikio
            - VAT: 18% kwa bidhaa na huduma
            - Kodi ya kampuni: 30% kwa kampuni
            - Kodi ya kuhifadhi: 15% kwa malipo fulani

            MIFANO YA UWEKEZAJI:
            - Treasury bonds: 10-15% faida
            - Dar es Salaam Stock Exchange (DSE)
            - Mali isiyohamishika: Dar es Salaam, Arusha, Mwanza
            - Unit trusts: NMB, CRDB, Stanbic

            MIFANO YA BANKKI:
            - CRDB Bank: Benki kubwa zaidi Tanzania
            - NMB Bank: Benki ya serikali
            - NBC Bank: Uwepo wa kimataifa
            - Benki ya simu: M-Pesa, Airtel Money

            MIFANO YA KANUNI:
            - Benki ya Tanzania (BoT): Benki kuu
            - Tanzania Revenue Authority (TRA): Uchukuaji wa kodi
            - Capital Markets and Securities Authority (CMSA)
            - Insurance Regulatory Authority (IRA)

            Daima jumuisha:
            1. Kiasi maalum kwa Shilingi za Tanzania
            2. Majina halisi ya benki za Tanzania na bidhaa
            3. Bei za soko la ndani na ada
            4. Kanuni za Tanzania na mahitaji
            5. Hatua za vitendo na taasisi za ndani
            6. Muktadha wa kitamaduni na mazoea ya ndani

            Ikiwa huna uhakika kuhusu kanuni maalum, 
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
            
            # Call OpenAI API with timeout and optimization
            client = openai.AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
            
            # Set timeout for the request
            timeout = 30  # seconds
            
            try:
                response = await asyncio.wait_for(
                    client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=openai_messages,
                        max_tokens=500,
                        temperature=0.7,
                        presence_penalty=0.1,
                        frequency_penalty=0.1,
                        timeout=timeout
                    ),
                    timeout=timeout
                )
                
                assistant_message = response.choices[0].message.content
                
            except asyncio.TimeoutError:
                logger.error("OpenAI API request timed out")
                assistant_message = "I apologize, but I'm taking longer than expected to respond. Please try again in a moment."
            except Exception as e:
                logger.error(f"OpenAI API error: {e}")
                assistant_message = "I'm experiencing technical difficulties. Please try again later."
            
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
        """Get conversation history with caching."""
        try:
            # Try to get from cache first
            cached_history = await get_cached_conversation_history(conversation_id)
            if cached_history:
                # Convert cached data back to ChatMessage objects
                messages = []
                for msg_data in cached_history:
                    message = ChatMessage(
                        id=msg_data['id'],
                        conversation_id=msg_data['conversation_id'],
                        role=msg_data['role'],
                        content=msg_data['content'],
                        timestamp=datetime.fromisoformat(msg_data['timestamp'])
                    )
                    messages.append(message)
                return messages
            
            # If not in cache, query database
            query = select(ChatMessage).where(
                ChatMessage.conversation_id == conversation_id
            ).order_by(ChatMessage.timestamp)
            
            result = await db.execute(query)
            messages = result.scalars().all()
            
            # Cache the conversation history
            if messages:
                history_data = []
                for msg in messages:
                    history_data.append({
                        'id': msg.id,
                        'conversation_id': msg.conversation_id,
                        'role': msg.role,
                        'content': msg.content,
                        'timestamp': msg.timestamp.isoformat()
                    })
                await cache_conversation_history(conversation_id, history_data)
            
            return messages
            
        except Exception as e:
            logger.error(f"Error getting conversation history: {e}")
            return []

    async def _get_relevant_knowledge(
        self, 
        db: AsyncSession, 
        user_message: str, 
        language: Language
    ) -> Optional[str]:
        """Get relevant knowledge base content with caching."""
        try:
            # Try to get from cache first
            cached_knowledge = await get_cached_knowledge_base(language.value)
            if cached_knowledge:
                # Use cached knowledge for keyword matching
                relevant_content = self._match_keywords_in_cached_knowledge(
                    user_message, cached_knowledge
                )
                if relevant_content:
                    return relevant_content
            
            # If not in cache, query database and cache results
            query = select(KnowledgeBase).where(
                KnowledgeBase.language == language.value,
                KnowledgeBase.is_active == True
            )
            
            result = await db.execute(query)
            knowledge_items = result.scalars().all()
            
            # Prepare knowledge for caching
            knowledge_dict = {}
            for item in knowledge_items:
                knowledge_dict[item.id] = {
                    'title': item.title,
                    'content': item.content,
                    'category': item.category,
                    'relevance_score': item.relevance_score
                }
            
            # Cache the knowledge base
            await cache_knowledge_base(language.value, knowledge_dict)
            
            # Match keywords in fresh data
            relevant_content = self._match_keywords_in_cached_knowledge(
                user_message, knowledge_dict
            )
            
            return relevant_content
            
        except Exception as e:
            logger.error(f"Error getting knowledge: {e}")
            return None

    def _match_keywords_in_cached_knowledge(
        self, 
        user_message: str, 
        knowledge_dict: dict
    ) -> Optional[str]:
        """Match keywords in cached knowledge base."""
        keywords = user_message.lower().split()
        relevant_content = []
        
        for item_id, item_data in knowledge_dict.items():
            content_lower = item_data['content'].lower()
            title_lower = item_data['title'].lower()
            
            # Check if any keywords match
            for keyword in keywords:
                if keyword in content_lower or keyword in title_lower:
                    relevant_content.append(f"{item_data['title']}: {item_data['content']}")
                    break
            
            # Limit to top 3 most relevant items
            if len(relevant_content) >= 3:
                break
        
        return "\n\n".join(relevant_content) if relevant_content else None

    async def _get_user_profile(
        self, 
        db: AsyncSession, 
        user_id: int
    ) -> Optional[Dict[str, Any]]:
        """Get user profile for personalization with caching."""
        try:
            # Try to get from cache first
            cached_profile = await get_cached_user_profile(user_id)
            if cached_profile:
                return cached_profile
            
            # If not in cache, query database
            query = select(User).where(User.id == user_id)
            result = await db.execute(query)
            user = result.scalar_one_or_none()
            
            if user:
                profile = {
                    'age_group': user.age_group,
                    'location': user.location,
                    'language': user.language
                }
                
                # Cache the user profile
                await cache_user_profile(user_id, profile)
                return profile
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