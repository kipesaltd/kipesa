-- Migration: Create chatbot tables
-- Date: 2024-01-XX

-- Create conversations table
CREATE TABLE IF NOT EXISTS conversations (
    id VARCHAR PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    language VARCHAR DEFAULT 'en',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    metadata JSONB
);

-- Create chat_messages table
CREATE TABLE IF NOT EXISTS chat_messages (
    id VARCHAR PRIMARY KEY,
    conversation_id VARCHAR NOT NULL REFERENCES conversations(id) ON DELETE CASCADE,
    role VARCHAR NOT NULL,
    content TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    metadata JSONB
);

-- Create chatbot_feedback table
CREATE TABLE IF NOT EXISTS chatbot_feedback (
    id VARCHAR PRIMARY KEY,
    conversation_id VARCHAR NOT NULL REFERENCES conversations(id) ON DELETE CASCADE,
    message_id VARCHAR NOT NULL REFERENCES chat_messages(id) ON DELETE CASCADE,
    rating INTEGER NOT NULL CHECK (rating >= 1 AND rating <= 5),
    feedback TEXT,
    helpful BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create chatbot_analytics table
CREATE TABLE IF NOT EXISTS chatbot_analytics (
    id VARCHAR PRIMARY KEY,
    conversation_id VARCHAR NOT NULL REFERENCES conversations(id) ON DELETE CASCADE,
    message_id VARCHAR NOT NULL REFERENCES chat_messages(id) ON DELETE CASCADE,
    intent VARCHAR,
    confidence FLOAT,
    entities JSONB,
    sentiment VARCHAR,
    response_time FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create knowledge_base table
CREATE TABLE IF NOT EXISTS knowledge_base (
    id VARCHAR PRIMARY KEY,
    title VARCHAR NOT NULL,
    content TEXT NOT NULL,
    category VARCHAR NOT NULL,
    language VARCHAR DEFAULT 'en',
    source VARCHAR,
    relevance_score FLOAT DEFAULT 1.0,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    metadata JSONB
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_conversations_user_id ON conversations(user_id);
CREATE INDEX IF NOT EXISTS idx_chat_messages_conversation_id ON chat_messages(conversation_id);
CREATE INDEX IF NOT EXISTS idx_chat_messages_timestamp ON chat_messages(timestamp);
CREATE INDEX IF NOT EXISTS idx_chatbot_feedback_conversation_id ON chatbot_feedback(conversation_id);
CREATE INDEX IF NOT EXISTS idx_chatbot_analytics_conversation_id ON chatbot_analytics(conversation_id);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_category ON knowledge_base(category);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_language ON knowledge_base(language);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_active ON knowledge_base(is_active);

-- Insert some initial knowledge base content for Tanzanian financial regulations
INSERT INTO knowledge_base (id, title, content, category, language, source, relevance_score) VALUES
(
    'kb-001',
    'Bank of Tanzania Regulations on Mobile Money',
    'The Bank of Tanzania regulates mobile money services through the National Payment Systems Act. All mobile money providers must be licensed and comply with anti-money laundering regulations. Transaction limits and fees are regulated to ensure consumer protection.',
    'regulation',
    'en',
    'Bank of Tanzania',
    1.0
),
(
    'kb-002',
    'TRA Tax Requirements for Small Businesses',
    'Small businesses in Tanzania must register for VAT if their annual turnover exceeds TSh 100 million. Income tax rates vary by business type and annual revenue. Proper record keeping is mandatory for all registered businesses.',
    'regulation',
    'en',
    'Tanzania Revenue Authority',
    1.0
),
(
    'kb-003',
    'Personal Finance Best Practices',
    'Create a budget that allocates 50% to needs, 30% to wants, and 20% to savings. Build an emergency fund covering 3-6 months of expenses. Diversify investments and avoid high-interest debt. Regularly review and adjust your financial plan.',
    'practice',
    'en',
    'Financial Education',
    1.0
),
(
    'kb-004',
    'Mikopo ya Benki na Masharti',
    'Mikopo ya benki inahitaji dhamana na historia nzuri ya mkopo. Kiwango cha riba kinategemea aina ya mkopo na muda. Hakikisha unaweza kulipa kila mwezi kabla ya kuomba mkopo.',
    'practice',
    'sw',
    'Financial Education',
    1.0
),
(
    'kb-005',
    'Investment Options in Tanzania',
    'Investment options include government bonds, corporate bonds, mutual funds, and real estate. Consider your risk tolerance and investment timeline. Diversification helps reduce risk. Consult with licensed financial advisors.',
    'practice',
    'en',
    'Financial Education',
    1.0
); 