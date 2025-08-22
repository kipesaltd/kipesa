#!/usr/bin/env python3
"""
Test Supabase connection pooling URL format.
"""

import asyncio
from app.core.config import get_settings

def test_connection_strings():
    """Test different Supabase connection string formats."""
    settings = get_settings()
    
    print("🔧 Testing different Supabase connection string formats...")
    
    # Current format (not working)
    current_url = settings.DATABASE_URL
    print(f"Current DATABASE_URL: {current_url}")
    
    # Alternative formats to try
    project_ref = "lzkewqoyosjgcnumykic"
    
    # Format 1: Direct connection (current - not working)
    format1 = f"postgresql+asyncpg://postgres:gaqcoh-Pipte2-ryddic@db.{project_ref}.supabase.co:5432/postgres"
    
    # Format 2: Connection pooling (recommended)
    format2 = f"postgresql+asyncpg://postgres:gaqcoh-Pipte2-ryddic@aws-0-{project_ref}.pooler.supabase.com:6543/postgres"
    
    # Format 3: Alternative pooling
    format3 = f"postgresql+asyncpg://postgres:gaqcoh-Pipte2-ryddic@aws-0-{project_ref}.pooler.supabase.com:5432/postgres"
    
    print(f"\nFormat 1 (Direct): {format1}")
    print(f"Format 2 (Pooling): {format2}")
    print(f"Format 3 (Alt Pooling): {format3}")
    
    print("\n💡 Recommendation:")
    print("Try using Format 2 (connection pooling) as it's more reliable for Supabase.")
    print("Update your .env file with:")
    print(f"DATABASE_URL={format2}")
    
    return [format1, format2, format3]

if __name__ == "__main__":
    test_connection_strings()

