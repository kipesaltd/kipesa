import redis.asyncio as redis
from aiocache import Cache, cached
from app.core.config import get_settings
import json
import pickle
from typing import Any, Optional
from loguru import logger

settings = get_settings()

# Redis connection with error handling
try:
    redis_client = redis.from_url(settings.REDIS_URL, decode_responses=True)
    logger.info("Redis connection established")
except Exception as e:
    logger.warning(f"Redis connection failed: {e}. Using in-memory fallback.")
    redis_client = None

class CacheManager:
    """Centralized cache management for the application."""
    
    def __init__(self):
        self.redis_client = redis_client
        self.default_ttl = 3600  # 1 hour
    
    async def get(self, key: str) -> Optional[Any]:
        """Get value from cache."""
        if not self.redis_client:
            logger.debug("Redis not available, skipping cache get")
            return None
            
        try:
            value = await self.redis_client.get(key)
            if value:
                return json.loads(value)
            return None
        except Exception as e:
            logger.error(f"Cache get error: {e}")
            return None
    
    async def set(self, key: str, value: Any, ttl: int = None) -> bool:
        """Set value in cache."""
        if not self.redis_client:
            logger.debug("Redis not available, skipping cache set")
            return False
            
        try:
            ttl = ttl or self.default_ttl
            await self.redis_client.setex(key, ttl, json.dumps(value))
            return True
        except Exception as e:
            logger.error(f"Cache set error: {e}")
            return False
    
    async def delete(self, key: str) -> bool:
        """Delete value from cache."""
        if not self.redis_client:
            logger.debug("Redis not available, skipping cache delete")
            return False
            
        try:
            await self.redis_client.delete(key)
            return True
        except Exception as e:
            logger.error(f"Cache delete error: {e}")
            return False
    
    async def exists(self, key: str) -> bool:
        """Check if key exists in cache."""
        if not self.redis_client:
            logger.debug("Redis not available, skipping cache exists check")
            return False
            
        try:
            return await self.redis_client.exists(key) > 0
        except Exception as e:
            logger.error(f"Cache exists error: {e}")
            return False

# Global cache manager instance
cache_manager = CacheManager()

# Cache decorators for specific use cases
@cached(ttl=3600, cache=Cache.MEMORY)
async def get_expensive_data(key: str):
    """Placeholder for expensive data retrieval with memory caching."""
    return f"Expensive data for {key}"

async def cache_knowledge_base(language: str, content: dict, ttl: int = 7200):
    """Cache knowledge base content."""
    key = f"knowledge_base:{language}"
    return await cache_manager.set(key, content, ttl)

async def get_cached_knowledge_base(language: str) -> Optional[dict]:
    """Get cached knowledge base content."""
    key = f"knowledge_base:{language}"
    return await cache_manager.get(key)

async def cache_conversation_history(conversation_id: str, messages: list, ttl: int = 1800):
    """Cache conversation history."""
    key = f"conversation:{conversation_id}"
    return await cache_manager.set(key, messages, ttl)

async def get_cached_conversation_history(conversation_id: str) -> Optional[list]:
    """Get cached conversation history."""
    key = f"conversation:{conversation_id}"
    return await cache_manager.get(key)

async def cache_user_profile(user_id: int, profile: dict, ttl: int = 3600):
    """Cache user profile."""
    key = f"user_profile:{user_id}"
    return await cache_manager.set(key, profile, ttl)

async def get_cached_user_profile(user_id: int) -> Optional[dict]:
    """Get cached user profile."""
    key = f"user_profile:{user_id}"
    return await cache_manager.get(key)
