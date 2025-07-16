from fastapi import APIRouter

router = APIRouter()


@router.post("/conversation")
async def start_conversation():
    """Start a new chatbot conversation."""
    pass


@router.post("/conversation/{conversation_id}")
async def continue_conversation(conversation_id: str):
    """Continue a chatbot conversation."""
    pass


@router.get("/conversation/{conversation_id}")
async def get_conversation_history(conversation_id: str):
    """Get conversation history."""
    pass
