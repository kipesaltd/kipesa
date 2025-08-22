#!/usr/bin/env python3
"""
Database initialization script for development.
Creates SQLite database and tables if they don't exist.
"""

import asyncio
import os
from sqlalchemy.ext.asyncio import create_async_engine
from app.db.models import Base

async def init_db():
    """Initialize the database with tables."""
    # Use SQLite for development
    database_url = "sqlite+aiosqlite:///./kipesa_dev.db"
    
    print(f"🔧 Initializing database: {database_url}")
    
    # Create engine
    engine = create_async_engine(
        database_url,
        echo=True,  # Enable SQL logging for debugging
        future=True
    )
    
    try:
        # Create all tables
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        print("✅ Database tables created successfully!")
        
    except Exception as e:
        print(f"❌ Error creating database tables: {e}")
        raise
    finally:
        await engine.dispose()

if __name__ == "__main__":
    print("🚀 Starting database initialization...")
    asyncio.run(init_db())
    print("✨ Database initialization complete!")

