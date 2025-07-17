from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from loguru import logger
from app.db.session import get_db_session


async def check_database_connection() -> bool:
    """Check if the database connection is healthy."""
    try:
        async with get_db_session() as session:
            # Simple query to test connection
            result = await session.execute(text("SELECT 1"))
            result.fetchone()
            logger.info("Database connection is healthy")
            return True
    except Exception as e:
        logger.error(f"Database connection check failed: {e}")
        return False


async def get_connection_info() -> dict:
    """Get database connection information for debugging."""
    try:
        async with get_db_session() as session:
            # Get PostgreSQL version and connection info
            result = await session.execute(text("SELECT version()"))
            version = result.scalar()
            
            # Get current connections
            result = await session.execute(text("""
                SELECT count(*) as active_connections 
                FROM pg_stat_activity 
                WHERE state = 'active'
            """))
            active_connections = result.scalar()
            
            return {
                "version": version,
                "active_connections": active_connections,
                "status": "healthy"
            }
    except Exception as e:
        logger.error(f"Failed to get connection info: {e}")
        return {
            "status": "unhealthy",
            "error": str(e)
        } 