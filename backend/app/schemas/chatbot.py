from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field


class Language(str, Enum):
    ENGLISH = "en"
    SWAHILI = "sw"


class MessageRole(str, Enum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"


class Message(BaseModel):
    role: MessageRole
    content: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    metadata: Optional[Dict[str, Any]] = None

    model_config = {
        "extra": "forbid"
    }


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=2000)
    conversation_id: Optional[str] = None
    language: Language = Language.ENGLISH
    user_id: Optional[str] = None
    context: Optional[Dict[str, Any]] = None

    model_config = {
        "extra": "forbid"
    }


class ChatResponse(BaseModel):
    conversation_id: str
    message: str
    language: Language
    confidence: float = Field(..., ge=0.0, le=1.0)
    intent: Optional[str] = None
    entities: Optional[List[Dict[str, Any]]] = None
    sentiment: Optional[str] = None
    response_time: float
    metadata: Optional[Dict[str, Any]] = None

    model_config = {
        "extra": "forbid"
    }


class ConversationCreate(BaseModel):
    initial_message: str = Field(..., min_length=1, max_length=2000)
    language: Language = Language.ENGLISH
    user_id: Optional[str] = None
    context: Optional[Dict[str, Any]] = None

    model_config = {
        "extra": "forbid"
    }


class ConversationResponse(BaseModel):
    conversation_id: str
    messages: List[Message]
    language: Language
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None

    model_config = {
        "extra": "forbid"
    }


class ConversationHistory(BaseModel):
    conversation_id: str
    messages: List[Message]
    total_messages: int
    created_at: datetime
    updated_at: datetime

    model_config = {
        "extra": "forbid"
    }


class ChatbotFeedback(BaseModel):
    conversation_id: str
    message_id: str
    rating: int = Field(..., ge=1, le=5)
    feedback: Optional[str] = None
    helpful: bool = True

    model_config = {
        "extra": "forbid"
    }


class ChatbotAnalytics(BaseModel):
    total_conversations: int
    total_messages: int
    average_response_time: float
    average_confidence: float
    language_distribution: Dict[str, int]
    top_intents: List[Dict[str, Any]]
    sentiment_distribution: Dict[str, int]

    model_config = {
        "extra": "forbid"
    }
