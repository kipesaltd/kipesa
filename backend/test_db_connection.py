#!/usr/bin/env python3
"""
Test script to verify Supabase database connection.
"""

import asyncio
from sqlalchemy import text
from app.db.models import engine

async def test_connection():
    """Test the database connection."""
    print("🔧 Testing Supabase database connection...")
    print(f"Database URL: {engine.url}")
    
    try:
        # Test basic connection
        async with engine.begin() as conn:
            print("✅ Database connection established successfully!")
            
            # Test a simple query
            result = await conn.execute(text("SELECT version()"))
            version = result.scalar()
            print(f"✅ Database query successful!")
            print(f"PostgreSQL version: {version}")
            
            # Test if we can access the users table
            result = await conn.execute(text("SELECT COUNT(*) FROM information_schema.tables WHERE table_name = 'users'"))
            table_count = result.scalar()
            print(f"✅ Users table exists: {table_count > 0}")
            
            if table_count > 0:
                # Try to count users
                result = await conn.execute(text("SELECT COUNT(*) FROM users"))
                user_count = result.scalar()
                print(f"✅ Users table accessible, count: {user_count}")
            
            print("🎉 All database tests passed!")
            
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        print(f"Error type: {type(e).__name__}")
        raise
    finally:
        await engine.dispose()

if __name__ == "__main__":
    asyncio.run(test_connection())

