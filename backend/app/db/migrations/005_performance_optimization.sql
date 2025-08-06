-- Migration: Performance Optimization Indexes
-- Date: 2024-01-XX

-- Add composite indexes for better query performance
CREATE INDEX IF NOT EXISTS idx_chat_messages_conversation_timestamp 
ON chat_messages(conversation_id, timestamp DESC);

CREATE INDEX IF NOT EXISTS idx_conversations_user_created 
ON conversations(user_id, created_at DESC);

CREATE INDEX IF NOT EXISTS idx_knowledge_base_language_active 
ON knowledge_base(language, is_active) WHERE is_active = true;

CREATE INDEX IF NOT EXISTS idx_knowledge_base_category_language 
ON knowledge_base(category, language, is_active);

-- Add full-text search index for knowledge base content
CREATE INDEX IF NOT EXISTS idx_knowledge_base_content_search 
ON knowledge_base USING gin(to_tsvector('english', title || ' ' || content));

-- Add index for analytics queries
CREATE INDEX IF NOT EXISTS idx_chatbot_analytics_conversation_created 
ON chatbot_analytics(conversation_id, created_at DESC);

CREATE INDEX IF NOT EXISTS idx_chatbot_analytics_intent_confidence 
ON chatbot_analytics(intent, confidence) WHERE confidence IS NOT NULL;

-- Add index for feedback queries
CREATE INDEX IF NOT EXISTS idx_chatbot_feedback_rating_created 
ON chatbot_feedback(rating, created_at DESC);

-- Add index for user queries
CREATE INDEX IF NOT EXISTS idx_users_email_language 
ON users(email, language);

-- Add partial indexes for active records
CREATE INDEX IF NOT EXISTS idx_knowledge_base_active_relevance 
ON knowledge_base(relevance_score DESC) WHERE is_active = true;

-- Add index for conversation language filtering
CREATE INDEX IF NOT EXISTS idx_conversations_language_created 
ON conversations(language, created_at DESC);

-- Add index for message role filtering
CREATE INDEX IF NOT EXISTS idx_chat_messages_role_timestamp 
ON chat_messages(role, timestamp DESC);

-- Add index for analytics sentiment analysis
CREATE INDEX IF NOT EXISTS idx_chatbot_analytics_sentiment_created 
ON chatbot_analytics(sentiment, created_at DESC) WHERE sentiment IS NOT NULL; 