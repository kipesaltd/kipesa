from datetime import datetime
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.services.auth import get_current_user_id
from app.services.chatbot import chatbot_service
from app.schemas.chatbot import (
    ChatRequest, ChatResponse, ConversationCreate, ConversationResponse,
    ConversationHistory, ChatbotFeedback, ChatbotAnalytics, Language
)

router = APIRouter()
security = HTTPBearer()


@router.post("/conversation", response_model=ConversationResponse, tags=["chatbot"])
async def start_conversation(
    conversation_data: ConversationCreate,
    db: AsyncSession = Depends(get_db),
    user_id: Optional[int] = None  # Make optional for testing
):
    """
    Start a new chatbot conversation.
    
    - **initial_message**: The first message from the user
    - **language**: Language preference (en/sw)
    - **user_id**: Optional user ID for personalization
    - **context**: Optional context data
    """
    try:
        response = await chatbot_service.create_conversation(
            db, conversation_data, user_id
        )
        return response
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to create conversation: {str(e)}"
        )


@router.post("/chat", response_model=ChatResponse, tags=["chatbot"])
async def send_message(
    chat_request: ChatRequest,
    db: AsyncSession = Depends(get_db),
    user_id: Optional[int] = None  # Make optional for testing
):
    """
    Send a message to the chatbot and get a response.
    
    - **message**: The user's message
    - **conversation_id**: Optional conversation ID (creates new if not provided)
    - **language**: Language preference (en/sw)
    - **user_id**: Optional user ID for personalization
    - **context**: Optional context data
    """
    try:
        response = await chatbot_service.process_message(
            db, chat_request, user_id
        )
        return response
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to process message: {str(e)}"
        )


@router.get("/conversation/{conversation_id}", response_model=ConversationHistory, tags=["chatbot"])
async def get_conversation_history(
    conversation_id: str,
    db: AsyncSession = Depends(get_db),
    user_id: Optional[int] = Depends(get_current_user_id)
):
    """
    Get conversation history by conversation ID.
    
    - **conversation_id**: The conversation ID to retrieve
    """
    try:
        conversation = await chatbot_service.get_conversation_history(db, conversation_id)
        if not conversation:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Conversation not found"
            )
        
        return ConversationHistory(
            conversation_id=conversation.conversation_id,
            messages=conversation.messages,
            total_messages=len(conversation.messages),
            created_at=conversation.created_at,
            updated_at=conversation.updated_at
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get conversation history: {str(e)}"
        )


@router.post("/feedback", tags=["chatbot"])
async def submit_feedback(
    feedback_data: ChatbotFeedback,
    db: AsyncSession = Depends(get_db),
    user_id: Optional[int] = Depends(get_current_user_id)
):
    """
    Submit feedback for a chatbot response.
    
    - **conversation_id**: The conversation ID
    - **message_id**: The message ID to provide feedback for
    - **rating**: Rating from 1-5
    - **feedback**: Optional text feedback
    - **helpful**: Whether the response was helpful
    """
    try:
        success = await chatbot_service.submit_feedback(db, feedback_data)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Failed to submit feedback"
            )
        
        return {"message": "Feedback submitted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to submit feedback: {str(e)}"
        )


@router.get("/analytics", response_model=ChatbotAnalytics, tags=["chatbot"])
async def get_chatbot_analytics(
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    db: AsyncSession = Depends(get_db),
    user_id: Optional[int] = Depends(get_current_user_id)
):
    """
    Get chatbot analytics.
    
    - **start_date**: Optional start date for analytics period
    - **end_date**: Optional end date for analytics period
    - **user_id**: Optional user ID for user-specific analytics
    """
    try:
        analytics = await chatbot_service.get_analytics(
            db, user_id, start_date, end_date
        )
        
        return ChatbotAnalytics(**analytics)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get analytics: {str(e)}"
        )


@router.get("/health", tags=["chatbot"])
async def chatbot_health():
    """
    Check chatbot service health.
    """
    try:
        # Basic health check - could be extended to check OpenAI API connectivity
        return {
            "status": "healthy",
            "timestamp": datetime.utcnow(),
            "service": "chatbot"
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Chatbot service unhealthy: {str(e)}"
        )


@router.get("/languages", tags=["chatbot"])
async def get_supported_languages():
    """
    Get list of supported languages.
    """
    return {
        "languages": [
            {"code": "en", "name": "English"},
            {"code": "sw", "name": "Swahili"}
        ]
    }


@router.get("/intents", tags=["chatbot"])
async def get_supported_intents():
    """
    Get list of supported intents.
    """
    return {
        "intents": [
            {"code": "budget_help", "name": "Budget Help", "description": "Help with budgeting and expense management"},
            {"code": "savings_advice", "name": "Savings Advice", "description": "Advice on saving money and investments"},
            {"code": "loan_advice", "name": "Loan Advice", "description": "Help with loans and credit"},
            {"code": "tax_help", "name": "Tax Help", "description": "Help with tax-related questions"},
            {"code": "regulation_info", "name": "Regulation Info", "description": "Information about financial regulations"},
            {"code": "greeting", "name": "Greeting", "description": "General greetings and introductions"},
            {"code": "general_help", "name": "General Help", "description": "General financial advice and assistance"}
        ]
    }
