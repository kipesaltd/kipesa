import uvicorn
from app.api import api_router
from app.core.config import get_settings
from app.core.error_handlers import add_error_handlers
from app.core.logging import setup_logging
from app.core.rate_limit import limiter
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi.middleware import SlowAPIMiddleware

settings = get_settings()

setup_logging()

app = FastAPI(title="Kipesa API", version="1.0.0")

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

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
