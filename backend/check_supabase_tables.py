#!/usr/bin/env python3
"""
Check existing tables in Supabase and create missing ones.
"""

import asyncio
from supabase import create_client, Client
from app.core.config import get_settings

async def check_and_create_tables():
    """Check existing tables and create missing ones."""
    settings = get_settings()
    
    print("🔧 Checking Supabase tables...")
    
    try:
        # Create Supabase client
        supabase: Client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
        print("✅ Supabase client created successfully!")
        
        # Check what tables exist
        try:
            # Try to get table info
            response = supabase.rpc('get_table_names').execute()
            print(f"✅ Tables found: {response}")
        except Exception as e:
            print(f"Could not get table names: {e}")
        
        # Try to create a simple test table
        print("\n🔧 Attempting to create tables...")
        
        # Create users table
        try:
            create_users_sql = """
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                email VARCHAR UNIQUE NOT NULL,
                hashed_password VARCHAR NOT NULL,
                full_name VARCHAR,
                phone_number VARCHAR UNIQUE,
                age_group VARCHAR,
                gender VARCHAR,
                location VARCHAR,
                language VARCHAR DEFAULT 'en',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """
            
            response = supabase.rpc('exec_sql', {'sql': create_users_sql}).execute()
            print("✅ Users table creation attempted")
            
        except Exception as e:
            print(f"❌ Could not create users table: {e}")
        
        # Test if we can now access the users table
        try:
            response = supabase.table('users').select('*').limit(1).execute()
            print("✅ Users table is now accessible!")
            print(f"Response: {response}")
        except Exception as e:
            print(f"❌ Users table still not accessible: {e}")
        
        print("\n🎉 Table check complete!")
        
    except Exception as e:
        print(f"❌ Supabase connection failed: {e}")
        raise

if __name__ == "__main__":
    asyncio.run(check_and_create_tables())

