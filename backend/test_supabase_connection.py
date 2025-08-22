#!/usr/bin/env python3
"""
Test script to verify Supabase connection using different methods.
"""

import asyncio
from supabase import create_client, Client
from app.core.config import get_settings

async def test_supabase_connection():
    """Test Supabase connection using the Supabase client."""
    settings = get_settings()
    
    print("🔧 Testing Supabase connection...")
    print(f"SUPABASE_URL: {settings.SUPABASE_URL}")
    print(f"SUPABASE_KEY: {settings.SUPABASE_KEY[:20]}...")
    
    try:
        # Test Supabase client connection
        supabase: Client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
        print("✅ Supabase client created successfully!")
        
        # Test a simple query using Supabase client
        response = supabase.table('users').select('*').limit(1).execute()
        print("✅ Supabase query successful!")
        print(f"Response: {response}")
        
        print("🎉 Supabase connection test passed!")
        
    except Exception as e:
        print(f"❌ Supabase connection failed: {e}")
        print(f"Error type: {type(e).__name__}")
        
        # Try to get more details about the error
        if hasattr(e, 'response'):
            print(f"Response status: {e.response.status_code}")
            print(f"Response body: {e.response.text}")
        
        raise

if __name__ == "__main__":
    asyncio.run(test_supabase_connection())

