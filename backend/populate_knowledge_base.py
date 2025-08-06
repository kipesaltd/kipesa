import asyncio
import asyncpg
from app.core.config import get_settings

settings = get_settings()

async def populate_knowledge_base():
    """Populate the knowledge base with Tanzanian-specific content."""
    
    # Connect to the database (fix URL format for asyncpg)
    db_url = settings.DATABASE_URL.replace('postgresql+asyncpg://', 'postgresql://')
    conn = await asyncpg.connect(db_url)
    
    try:
        # Read the migration SQL file
        with open('app/db/migrations/004_enhance_knowledge_base.sql', 'r') as f:
            sql_content = f.read()
        
        # Split into individual statements and execute
        statements = [stmt.strip() for stmt in sql_content.split(';') if stmt.strip()]
        
        for statement in statements:
            if statement:
                await conn.execute(statement)
        
        print("✅ Knowledge base populated successfully!")
        
        # Verify the data was inserted
        count = await conn.fetchval("SELECT COUNT(*) FROM knowledge_base")
        print(f"📊 Total knowledge base entries: {count}")
        
        # Show some sample entries
        entries = await conn.fetch("SELECT title, category, language FROM knowledge_base LIMIT 5")
        print("\n📋 Sample entries:")
        for entry in entries:
            print(f"  - {entry['title']} ({entry['category']}, {entry['language']})")
            
    except Exception as e:
        print(f"❌ Error populating knowledge base: {e}")
        raise
    finally:
        await conn.close()

if __name__ == "__main__":
    asyncio.run(populate_knowledge_base()) 