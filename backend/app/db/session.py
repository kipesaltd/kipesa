from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from loguru import logger
from app.db.models import AsyncSessionLocal
import asyncio


@asynccontextmanager
async def get_db_session():
    """Get a database session with proper error handling and connection management."""
    session = AsyncSessionLocal()
    max_retries = 3
    retry_delay = 1  # seconds
    
    for attempt in range(max_retries):
        try:
            yield session
            await session.commit()
            break
        except SQLAlchemyError as e:
            await session.rollback()
            logger.error(f"Database error (attempt {attempt + 1}/{max_retries}): {e}")
            
            if attempt < max_retries - 1:
                logger.info(f"Retrying database operation in {retry_delay} seconds...")
                await asyncio.sleep(retry_delay)
                retry_delay *= 2  # Exponential backoff
            else:
                logger.error("Max retries reached, giving up")
                raise
        except Exception as e:
            await session.rollback()
            logger.error(f"Unexpected database error: {e}")
            raise
        finally:
            if attempt == max_retries - 1:  # Only close on final attempt
                await session.close()


async def get_db():
    """FastAPI dependency for database sessions."""
    async with get_db_session() as session:
        yield session 