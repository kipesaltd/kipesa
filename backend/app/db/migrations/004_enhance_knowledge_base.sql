-- Migration: Enhance knowledge base with Tanzanian-specific content
-- Date: 2024-01-XX

-- Clear existing knowledge base data
DELETE FROM knowledge_base;

-- Insert comprehensive Tanzanian financial knowledge base

-- BUDGETING AND PERSONAL FINANCE
INSERT INTO knowledge_base (id, title, content, category, language, source, relevance_score) VALUES
(
    'kb-budget-001',
    'Monthly Budget Template for Tanzania',
    'Sample monthly budget for TSh 800,000 salary in Dar es Salaam:
    
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
    - Miscellaneous: TSh 20,000',
    'budgeting',
    'en',
    'Kipesa Financial Education',
    1.0
),
(
    'kb-budget-002',
    'Bajeti ya Mwezi kwa Tanzania',
    'Mfano wa bajeti ya mwezi kwa mshahara wa TSh 800,000 Dar es Salaam:
    
    **Mapato: TSh 800,000**
    
    **Gharama Muhimu (50% - TSh 400,000):**
    - Kodi ya nyumba: TSh 300,000
    - Chakula: TSh 150,000
    - Usafiri (daladala): TSh 50,000
    
    **Huduma za Msingi (10% - TSh 80,000):**
    - Umeme: TSh 30,000
    - Maji: TSh 15,000
    - Internet: TSh 20,000
    - Simu: TSh 15,000
    
    **Kuweka Pesa (20% - TSh 160,000):**
    - Mfuko wa dharura: TSh 100,000
    - Uwekezaji: TSh 60,000
    
    **Matumizi ya Hiari (20% - TSh 160,000):**
    - Burudani: TSh 50,000
    - Kununua: TSh 60,000
    - Afya: TSh 30,000
    - Zingine: TSh 20,000',
    'budgeting',
    'sw',
    'Kipesa Financial Education',
    1.0
),

-- SAVINGS AND INVESTMENT
INSERT INTO knowledge_base (id, title, content, category, language, source, relevance_score) VALUES
(
    'kb-savings-001',
    'Emergency Fund Building in Tanzania',
    '**Emergency Fund Guidelines:**
    
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
    
    **Total Emergency Fund:** TSh 1,950,000 (6 months)',
    'savings',
    'en',
    'Kipesa Financial Education',
    1.0
),
(
    'kb-savings-002',
    'Investment Options in Tanzania',
    '**Tanzanian Investment Options:**
    
    **1. Government Treasury Bonds:**
    - Minimum: TSh 100,000
    - Returns: 10-15% annually
    - Duration: 2-10 years
    - Risk: Low
    
    **2. Dar es Salaam Stock Exchange (DSE):**
    - Popular stocks: CRDB, NMB, TBL, TCC
    - Minimum investment: TSh 50,000
    - Returns: 5-20% annually
    - Risk: Medium
    
    **3. Real Estate:**
    - Dar es Salaam: TSh 50M - 200M
    - Arusha: TSh 30M - 100M
    - Mwanza: TSh 25M - 80M
    - Returns: 8-15% annually
    
    **4. Unit Trusts:**
    - NMB Unit Trust: 8-12% returns
    - CRDB Unit Trust: 7-11% returns
    - Stanbic Unit Trust: 9-13% returns
    - Minimum: TSh 50,000
    
    **5. Fixed Deposits:**
    - CRDB: 8-12% interest
    - NMB: 9-13% interest
    - NBC: 7-11% interest
    - Duration: 3 months - 5 years',
    'investment',
    'en',
    'Kipesa Financial Education',
    1.0
),

-- LOANS AND CREDIT
INSERT INTO knowledge_base (id, title, content, category, language, source, relevance_score) VALUES
(
    'kb-loans-001',
    'Personal Loan Options in Tanzania',
    '**Personal Loan Comparison:**
    
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
    
    **NBC Bank Personal Loan:**
    - Interest rate: 16-19%
    - Maximum amount: TSh 25M
    - Repayment period: 12-36 months
    - Requirements: NBC account, guarantor
    
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
    - Total interest: TSh 1M',
    'loans',
    'en',
    'Kipesa Financial Education',
    1.0
),
(
    'kb-loans-002',
    'Business Loan Options for SMEs',
    '**SME Loan Options:**
    
    **NMB Business Loan:**
    - Interest rate: 12-16%
    - Maximum amount: TSh 100M
    - Repayment period: 12-60 months
    - Requirements: Business plan, collateral
    
    **CRDB Business Loan:**
    - Interest rate: 13-17%
    - Maximum amount: TSh 200M
    - Repayment period: 12-72 months
    - Requirements: Business registration, financial statements
    
    **SELFINA Microfinance:**
    - Interest rate: 18-24%
    - Maximum amount: TSh 10M
    - Repayment period: 6-24 months
    - Requirements: Group guarantee, business training
    
    **PRIDE Tanzania:**
    - Interest rate: 20-25%
    - Maximum amount: TSh 5M
    - Repayment period: 6-18 months
    - Requirements: Group membership, savings history',
    'loans',
    'en',
    'Kipesa Financial Education',
    1.0
),

-- TAXES AND REGULATIONS
INSERT INTO knowledge_base (id, title, content, category, language, source, relevance_score) VALUES
(
    'kb-tax-001',
    'Income Tax (PAYE) in Tanzania',
    '**PAYE Tax Rates (2024):**
    
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
    - **Net Salary: TSh 722,000**
    
    **Salary: TSh 1,500,000/month**
    - First TSh 270,000: TSh 0
    - TSh 270,001 - 520,000: TSh 20,000 (8%)
    - TSh 520,001 - 760,000: TSh 48,000 (20%)
    - TSh 760,001 - 1,000,000: TSh 60,000 (25%)
    - TSh 1,000,001 - 1,500,000: TSh 150,000 (30%)
    - **Total Tax: TSh 278,000**
    - **Net Salary: TSh 1,222,000**',
    'tax',
    'en',
    'Tanzania Revenue Authority',
    1.0
),
(
    'kb-tax-002',
    'VAT Requirements for Businesses',
    '**VAT Registration Requirements:**
    
    **Mandatory Registration:**
    - Annual turnover exceeds TSh 100M
    - Import/export businesses
    - Digital service providers
    
    **VAT Rate:** 18%
    
    **Example VAT Calculation:**
    
    **Business sells goods worth TSh 1,000,000:**
    - Selling price: TSh 1,000,000
    - VAT (18%): TSh 180,000
    - Total price: TSh 1,180,000
    
    **Business buys goods worth TSh 500,000:**
    - Purchase price: TSh 500,000
    - Input VAT: TSh 90,000
    - Net VAT payable: TSh 90,000 (180,000 - 90,000)
    
    **VAT Filing:**
    - Monthly returns
    - Due date: 20th of following month
    - Penalty for late filing: TSh 100,000',
    'tax',
    'en',
    'Tanzania Revenue Authority',
    1.0
),

-- BANKING AND MOBILE MONEY
INSERT INTO knowledge_base (id, title, content, category, language, source, relevance_score) VALUES
(
    'kb-banking-001',
    'Bank Account Comparison in Tanzania',
    '**Major Banks in Tanzania:**
    
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
    - ATM withdrawal: TSh 1,500
    
    **Stanbic Bank:**
    - Savings account: 4-6% interest
    - Current account: No interest
    - Minimum balance: TSh 20,000
    - Monthly fee: TSh 10,000
    - ATM withdrawal: TSh 2,000',
    'banking',
    'en',
    'Kipesa Financial Education',
    1.0
),
(
    'kb-banking-002',
    'Mobile Money Services in Tanzania',
    '**Mobile Money Comparison:**
    
    **M-Pesa (Vodacom):**
    - Market share: 60%
    - Transaction fee: TSh 100-1,000
    - Daily limit: TSh 3M
    - Monthly limit: TSh 7M
    - Savings: 0% interest
    
    **Airtel Money (Airtel):**
    - Market share: 25%
    - Transaction fee: TSh 50-800
    - Daily limit: TSh 2M
    - Monthly limit: TSh 5M
    - Savings: 0% interest
    
    **Tigo Pesa (Tigo):**
    - Market share: 15%
    - Transaction fee: TSh 75-900
    - Daily limit: TSh 1.5M
    - Monthly limit: TSh 4M
    - Savings: 0% interest
    
    **Transaction Fees Example:**
    - Send TSh 10,000: TSh 100
    - Send TSh 50,000: TSh 300
    - Send TSh 100,000: TSh 500
    - Send TSh 500,000: TSh 1,000',
    'banking',
    'en',
    'Kipesa Financial Education',
    1.0
),

-- INSURANCE AND PROTECTION
INSERT INTO knowledge_base (id, title, content, category, language, source, relevance_score) VALUES
(
    'kb-insurance-001',
    'Insurance Options in Tanzania',
    '**Insurance Products Available:**
    
    **Health Insurance:**
    - NHIF (National): TSh 3,000/month
    - Private health: TSh 20,000-50,000/month
    - Coverage: 80-100% of medical costs
    
    **Life Insurance:**
    - Term life: TSh 5,000-20,000/month
    - Whole life: TSh 10,000-30,000/month
    - Coverage: TSh 10M - 100M
    
    **Motor Insurance:**
    - Third party: TSh 50,000-100,000/year
    - Comprehensive: TSh 200,000-500,000/year
    - Coverage: Vehicle damage, third party
    
    **Property Insurance:**
    - Home insurance: TSh 100,000-300,000/year
    - Business insurance: TSh 200,000-1M/year
    - Coverage: Fire, theft, natural disasters
    
    **Travel Insurance:**
    - Local travel: TSh 10,000-30,000/trip
    - International: TSh 50,000-200,000/trip
    - Coverage: Medical, luggage, cancellation',
    'insurance',
    'en',
    'Kipesa Financial Education',
    1.0
),

-- RETIREMENT PLANNING
INSERT INTO knowledge_base (id, title, content, category, language, source, relevance_score) VALUES
(
    'kb-retirement-001',
    'Retirement Planning in Tanzania',
    '**Retirement Planning Guide:**
    
    **Government Pension (NSSF):**
    - Employee contribution: 10% of salary
    - Employer contribution: 10% of salary
    - Retirement age: 60 years
    - Lump sum payment at retirement
    
    **Private Pension Plans:**
    - NSSF Private: 5-15% of salary
    - Insurance company plans: TSh 50,000-200,000/month
    - Investment-based plans: Variable contributions
    
    **Retirement Savings Calculation:**
    
    **Example: 30-year-old earning TSh 1M/month**
    - Monthly savings: TSh 200,000
    - Annual savings: TSh 2.4M
    - Investment return: 10% annually
    - Retirement age: 60 years
    
    **At retirement (30 years):**
    - Total savings: TSh 72M
    - Investment growth: TSh 400M
    - Total retirement fund: TSh 472M
    
    **Monthly retirement income:**
    - 4% withdrawal rate: TSh 1.6M/month
    - 6% withdrawal rate: TSh 2.4M/month',
    'retirement',
    'en',
    'Kipesa Financial Education',
    1.0
),

-- STUDENT LOANS AND EDUCATION
INSERT INTO knowledge_base (id, title, content, category, language, source, relevance_score) VALUES
(
    'kb-education-001',
    'Student Loan Options in Tanzania',
    '**Higher Education Student Loans Board (HESLB):**
    
    **Eligibility:**
    - Tanzanian citizen
    - Admitted to accredited institution
    - Family income below TSh 3M/year
    
    **Loan Amounts:**
    - Tuition fees: Full coverage
    - Accommodation: TSh 200,000-400,000/year
    - Books and supplies: TSh 100,000-200,000/year
    - Meals: TSh 300,000-500,000/year
    
    **Repayment:**
    - Start: 6 months after graduation
    - Interest rate: 0% (government subsidized)
    - Repayment period: 10-15 years
    - Monthly payment: Based on salary
    
    **Example Repayment:**
    - Loan amount: TSh 15M
    - Starting salary: TSh 800,000/month
    - Monthly payment: TSh 150,000
    - Repayment period: 10 years
    
    **Private Student Loans:**
    - CRDB Education Loan: 12-15% interest
    - NMB Education Loan: 11-14% interest
    - Maximum amount: TSh 20M
    - Repayment period: 5-10 years',
    'education',
    'en',
    'Kipesa Financial Education',
    1.0
),

-- BUSINESS FINANCE
INSERT INTO knowledge_base (id, title, content, category, language, source, relevance_score) VALUES
(
    'kb-business-001',
    'Starting a Business in Tanzania',
    '**Business Registration Costs:**
    
    **Sole Proprietorship:**
    - Registration: TSh 50,000
    - Business license: TSh 100,000-500,000
    - Tax registration: Free
    - Total: TSh 150,000-550,000
    
    **Limited Company:**
    - Registration: TSh 200,000
    - Business license: TSh 200,000-1M
    - Tax registration: Free
    - Legal fees: TSh 500,000-1M
    - Total: TSh 900,000-2.2M
    
    **Business Bank Account:**
    - CRDB: TSh 50,000 opening
    - NMB: TSh 25,000 opening
    - NBC: TSh 100,000 opening
    - Monthly fees: TSh 10,000-20,000
    
    **Common Business Types:**
    - Retail shop: TSh 5M-20M startup
    - Restaurant: TSh 10M-50M startup
    - Transport business: TSh 20M-100M startup
    - Manufacturing: TSh 50M-500M startup
    
    **Funding Sources:**
    - Personal savings: 40-60%
    - Bank loans: 20-40%
    - Family/friends: 10-20%
    - Investors: 10-30%',
    'business',
    'en',
    'Kipesa Financial Education',
    1.0
),

-- REAL ESTATE
INSERT INTO knowledge_base (id, title, content, category, language, source, relevance_score) VALUES
(
    'kb-realestate-001',
    'Real Estate Investment in Tanzania',
    '**Property Prices by Location:**
    
    **Dar es Salaam:**
    - 1-bedroom apartment: TSh 50M-100M
    - 2-bedroom apartment: TSh 80M-150M
    - 3-bedroom house: TSh 150M-300M
    - Commercial property: TSh 200M-1B
    
    **Arusha:**
    - 1-bedroom apartment: TSh 30M-60M
    - 2-bedroom apartment: TSh 50M-100M
    - 3-bedroom house: TSh 100M-200M
    - Commercial property: TSh 100M-500M
    
    **Mwanza:**
    - 1-bedroom apartment: TSh 25M-50M
    - 2-bedroom apartment: TSh 40M-80M
    - 3-bedroom house: TSh 80M-150M
    - Commercial property: TSh 80M-400M
    
    **Mortgage Options:**
    - CRDB: 15-18% interest, 20-year term
    - NMB: 14-17% interest, 25-year term
    - NBC: 16-19% interest, 15-year term
    
    **Example Mortgage:**
    - Property price: TSh 100M
    - Down payment: TSh 20M (20%)
    - Loan amount: TSh 80M
    - Interest rate: 16%
    - Term: 20 years
    - Monthly payment: TSh 1.2M',
    'realestate',
    'en',
    'Kipesa Financial Education',
    1.0
);

-- Swahili versions of key content
INSERT INTO knowledge_base (id, title, content, category, language, source, relevance_score) VALUES
(
    'kb-savings-003',
    'Kuweka Pesa na Uwekezaji Tanzania',
    '**Chaguo za Kuweka Pesa:**
    
    **1. Treasury Bonds ya Serikali:**
    - Kiasi cha chini: TSh 100,000
    - Faida: 10-15% kwa mwaka
    - Muda: Miaka 2-10
    - Hatari: Chini
    
    **2. Dar es Salaam Stock Exchange (DSE):**
    - Hissha maarufu: CRDB, NMB, TBL, TCC
    - Uwekezaji wa chini: TSh 50,000
    - Faida: 5-20% kwa mwaka
    - Hatari: Kati
    
    **3. Mali Isiyohamishika:**
    - Dar es Salaam: TSh 50M - 200M
    - Arusha: TSh 30M - 100M
    - Mwanza: TSh 25M - 80M
    - Faida: 8-15% kwa mwaka
    
    **4. Unit Trusts:**
    - NMB Unit Trust: 8-12% faida
    - CRDB Unit Trust: 7-11% faida
    - Stanbic Unit Trust: 9-13% faida
    - Kiasi cha chini: TSh 50,000',
    'investment',
    'sw',
    'Kipesa Financial Education',
    1.0
),
(
    'kb-loans-003',
    'Mikopo ya Kibinafsi Tanzania',
    '**Mlinganisho wa Mikopo:**
    
    **Mikopo ya CRDB Bank:**
    - Kiwango cha riba: 15-18%
    - Kiasi cha juu: TSh 50M
    - Muda wa kulipa: Miezi 12-60
    - Mahitaji: Akaunti ya mshahara, kazi miezi 3
    
    **Mikopo ya NMB Bank:**
    - Kiwango cha riba: 14-17%
    - Kiasi cha juu: TSh 30M
    - Muda wa kulipa: Miezi 12-48
    - Mahitaji: Akaunti ya NMB, payslip
    
    **Mikopo ya M-Pesa:**
    - Kiwango cha riba: 5-10% (kwa siku)
    - Kiasi cha juu: TSh 1M
    - Muda wa kulipa: Siku 30
    - Mahitaji: Akaunti ya M-Pesa, historia nzuri',
    'loans',
    'sw',
    'Kipesa Financial Education',
    1.0
); 