from typing import List, Optional

from pydantic import BaseModel


class Message(BaseModel):
    sender: str
    content: str
    timestamp: str

    model_config = {
        "extra": "forbid"
    }


class ConversationCreate(BaseModel):
    initial_message: str
    language: Optional[str] = 'en'

    model_config = {
        "extra": "forbid"
    }


class ConversationResponse(BaseModel):
    conversation_id: str
    messages: List[Message]

    model_config = {
        "extra": "forbid"
    }
