import uvicorn
from app.api import api_router
from app.core.config import get_settings
from app.core.error_handlers import add_error_handlers
from app.core.logging import setup_logging
from app.core.rate_limit import limiter
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from slowapi.middleware import SlowAPIMiddleware

settings = get_settings()

setup_logging()

app = FastAPI(
    title="Kipesa API", 
    version="1.0.0",
    description="Kipesa Finance Platform API",
    openapi_tags=[
        {"name": "auth", "description": "Authentication operations"},
        {"name": "finance", "description": "Financial data operations"},
        {"name": "chatbot", "description": "AI chatbot operations"},
        {"name": "calculators", "description": "Financial calculator operations"},
        {"name": "content", "description": "Content management operations"},
        {"name": "health", "description": "Health check operations"},
    ]
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rate Limiting
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

# Routers
app.include_router(api_router)

# Error Handlers
add_error_handlers(app)


def custom_openapi():
    """Custom OpenAPI schema with security definitions."""
    if app.openapi_schema:
        return app.openapi_schema
    
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )
    
    # Add security schemes
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }
    
    # Don't apply global security - let each endpoint define its own requirements
    # This allows some endpoints to be public while others require authentication
    
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
