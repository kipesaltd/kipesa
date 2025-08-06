import asyncio
import asyncpg
from app.core.config import get_settings

settings = get_settings()

# Knowledge base data
KNOWLEDGE_BASE_DATA = [
    {
        'id': 'kb-budget-001',
        'title': 'Monthly Budget Template for Tanzania',
        'content': '''Sample monthly budget for TSh 800,000 salary in Dar es Salaam:

**Income: TSh 800,000**

**Essential Expenses (50% - TSh 400,000):**
- Rent: TSh 300,000
- Food: TSh 150,000
- Transport (daladala): TSh 50,000

**Utilities (10% - TSh 80,000):**
- Electricity: TSh 30,000
- Water: TSh 15,000
- Internet: TSh 20,000
- Phone: TSh 15,000

**Savings (20% - TSh 160,000):**
- Emergency fund: TSh 100,000
- Investment: TSh 60,000

**Discretionary (20% - TSh 160,000):**
- Entertainment: TSh 50,000
- Shopping: TSh 60,000
- Healthcare: TSh 30,000
- Miscellaneous: TSh 20,000''',
        'category': 'budgeting',
        'language': 'en',
        'source': 'Kipesa Financial Education',
        'relevance_score': 1.0
    },
    {
        'id': 'kb-savings-001',
        'title': 'Emergency Fund Building in Tanzania',
        'content': '''**Emergency Fund Guidelines:**

**Target Amount:** 3-6 months of essential expenses

**Example for Dar es Salaam resident:**
- Monthly essential expenses: TSh 500,000
- Emergency fund target: TSh 1.5M - 3M

**Where to Save:**
1. **M-Pesa Savings:** 0% interest, instant access
2. **CRDB Savings Account:** 5-7% interest
3. **NMB Savings Account:** 6-8% interest
4. **NBC Savings Account:** 5-6% interest

**Monthly Savings Plan:**
- Month 1-3: TSh 100,000/month = TSh 300,000
- Month 4-6: TSh 150,000/month = TSh 450,000
- Month 7-12: TSh 200,000/month = TSh 1,200,000

**Total Emergency Fund:** TSh 1,950,000 (6 months)''',
        'category': 'savings',
        'language': 'en',
        'source': 'Kipesa Financial Education',
        'relevance_score': 1.0
    },
    {
        'id': 'kb-loans-001',
        'title': 'Personal Loan Options in Tanzania',
        'content': '''**Personal Loan Comparison:**

**CRDB Bank Personal Loan:**
- Interest rate: 15-18%
- Maximum amount: TSh 50M
- Repayment period: 12-60 months
- Requirements: Salary account, 3 months employment

**NMB Bank Personal Loan:**
- Interest rate: 14-17%
- Maximum amount: TSh 30M
- Repayment period: 12-48 months
- Requirements: NMB account, payslip

**M-Pesa Loan:**
- Interest rate: 5-10% (daily)
- Maximum amount: TSh 1M
- Repayment period: 30 days
- Requirements: M-Pesa account, good history

**Example Calculation:**
- Loan amount: TSh 5M
- Interest rate: 16%
- Duration: 24 months
- Monthly payment: TSh 250,000
- Total interest: TSh 1M''',
        'category': 'loans',
        'language': 'en',
        'source': 'Kipesa Financial Education',
        'relevance_score': 1.0
    },
    {
        'id': 'kb-tax-001',
        'title': 'Income Tax (PAYE) in Tanzania',
        'content': '''**PAYE Tax Rates (2024):**

**Monthly Income Tax Brackets:**

**TSh 0 - 270,000:** 0%
**TSh 270,001 - 520,000:** 8%
**TSh 520,001 - 760,000:** 20%
**TSh 760,001 - 1,000,000:** 25%
**Above TSh 1,000,000:** 30%

**Example Calculations:**

**Salary: TSh 800,000/month**
- First TSh 270,000: TSh 0
- TSh 270,001 - 520,000: TSh 20,000 (8%)
- TSh 520,001 - 760,000: TSh 48,000 (20%)
- TSh 760,001 - 800,000: TSh 10,000 (25%)
- **Total Tax: TSh 78,000**
- **Net Salary: TSh 722,000**''',
        'category': 'tax',
        'language': 'en',
        'source': 'Tanzania Revenue Authority',
        'relevance_score': 1.0
    },
    {
        'id': 'kb-banking-001',
        'title': 'Bank Account Comparison in Tanzania',
        'content': '''**Major Banks in Tanzania:**

**CRDB Bank (Largest):**
- Savings account: 5-7% interest
- Current account: No interest
- Minimum balance: TSh 10,000
- Monthly fee: TSh 5,000
- ATM withdrawal: TSh 1,000

**NMB Bank (Government-owned):**
- Savings account: 6-8% interest
- Current account: No interest
- Minimum balance: TSh 5,000
- Monthly fee: TSh 3,000
- ATM withdrawal: TSh 500

**NBC Bank (International):**
- Savings account: 5-6% interest
- Current account: No interest
- Minimum balance: TSh 15,000
- Monthly fee: TSh 7,000
- ATM withdrawal: TSh 1,500''',
        'category': 'banking',
        'language': 'en',
        'source': 'Kipesa Financial Education',
        'relevance_score': 1.0
    }
]

async def populate_knowledge_base():
    """Populate the knowledge base with Tanzanian-specific content."""
    
    # Connect to the database (fix URL format for asyncpg)
    db_url = settings.DATABASE_URL.replace('postgresql+asyncpg://', 'postgresql://')
    conn = await asyncpg.connect(db_url)
    
    try:
        # Clear existing data
        await conn.execute("DELETE FROM knowledge_base")
        print("🗑️  Cleared existing knowledge base data")
        
        # Insert new data
        for item in KNOWLEDGE_BASE_DATA:
            await conn.execute("""
                INSERT INTO knowledge_base (id, title, content, category, language, source, relevance_score)
                VALUES ($1, $2, $3, $4, $5, $6, $7)
            """, item['id'], item['title'], item['content'], item['category'], 
                 item['language'], item['source'], item['relevance_score'])
        
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