from fastapi import APIRouter

from . import auth, calculators, chatbot, content, finance, health

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(chatbot.router, prefix="/chatbot", tags=["chatbot"])
api_router.include_router(
    calculators.router, prefix="/calculators", tags=["calculators"]
)
api_router.include_router(finance.router, prefix="/finance", tags=["finance"])
api_router.include_router(content.router, prefix="/content", tags=["content"])
api_router.include_router(health.router, prefix="/health", tags=["health"])
