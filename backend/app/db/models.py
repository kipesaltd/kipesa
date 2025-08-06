import datetime
import uuid
from typing import Optional

from app.core.config import get_settings
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text, Float, Boolean, JSON
from sqlalchemy.ext.asyncio import (AsyncAttrs, async_sessionmaker,
                                    create_async_engine)
from sqlalchemy.orm import declarative_base
from sqlalchemy.pool import NullPool

settings = get_settings()

DATABASE_URL = settings.DATABASE_URL

# Configure engine with optimized connection pool settings
if "supabase" in DATABASE_URL.lower():
    # Supabase uses NullPool - no pool parameters allowed
    engine = create_async_engine(
        DATABASE_URL,
        echo=False,  # Disable SQL logging in production
        future=True,
        pool_pre_ping=True,  # Verify connections before use
        pool_recycle=3600,   # Recycle connections after 1 hour
        poolclass=NullPool
    )
else:
    # Regular database with connection pooling
    engine = create_async_engine(
        DATABASE_URL,
        echo=False,  # Disable SQL logging in production
        future=True,
        pool_pre_ping=True,  # Verify connections before use
        pool_recycle=3600,   # Recycle connections after 1 hour
        pool_size=20,         # Maximum number of connections in pool
        max_overflow=30,      # Additional connections beyond pool_size
        pool_timeout=30       # Timeout for getting connection from pool
    )

# Configure session with proper settings
AsyncSessionLocal = async_sessionmaker(
    engine,
    expire_on_commit=False,
    autoflush=False,
    autocommit=False
)

Base = declarative_base(cls=AsyncAttrs)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String)
    phone_number = Column(String, unique=True, index=True, nullable=True)
    age_group = Column(
        String, nullable=True
    )  # e.g., '18-25', '26-35', etc.
    gender = Column(
        String, nullable=True
    )  # e.g., 'male', 'female', 'other'
    location = Column(
        String, nullable=True
    )  # To be set via device IP geo-lookup
    language = Column(String, default="en")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)


class IncomeSource(Base):
    __tablename__ = "income_sources"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    name = Column(
        String, nullable=False
    )
    amount = Column(
        Integer, nullable=False
    )
    frequency = Column(
        String, nullable=True
    )  # e.g., 'monthly', 'weekly'
    description = Column(
        Text, nullable=True
    )
    created_at = Column(
        DateTime, default=datetime.datetime.utcnow
    )


class Expense(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    amount = Column(Integer, nullable=False)
    category = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)


class Budget(Base):
    __tablename__ = "budgets"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    amount = Column(Integer, nullable=False)
    category = Column(String, nullable=False)
    period = Column(String, nullable=False)  # e.g., 'monthly', 'yearly'
    created_at = Column(DateTime, default=datetime.datetime.utcnow)


class SavingsGoal(Base):
    __tablename__ = "savings_goals"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    target_amount = Column(Integer, nullable=False)
    description = Column(Text, nullable=True)
    target_date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)


# Chatbot Models
class Conversation(Base):
    __tablename__ = "conversations"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True, index=True)
    language = Column(String, default="en")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    meta_data = Column(JSON, nullable=True)


class ChatMessage(Base):
    __tablename__ = "chat_messages"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    conversation_id = Column(String, ForeignKey("conversations.id"), nullable=False, index=True)
    role = Column(String, nullable=False)  # 'user', 'assistant', 'system'
    content = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    meta_data = Column(JSON, nullable=True)


class ChatbotFeedback(Base):
    __tablename__ = "chatbot_feedback"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    conversation_id = Column(String, ForeignKey("conversations.id"), nullable=False, index=True)
    message_id = Column(String, ForeignKey("chat_messages.id"), nullable=False, index=True)
    rating = Column(Integer, nullable=False)  # 1-5 scale
    feedback = Column(Text, nullable=True)
    helpful = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)


class ChatbotAnalytics(Base):
    __tablename__ = "chatbot_analytics"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    conversation_id = Column(String, ForeignKey("conversations.id"), nullable=False, index=True)
    message_id = Column(String, ForeignKey("chat_messages.id"), nullable=False, index=True)
    intent = Column(String, nullable=True)
    confidence = Column(Float, nullable=True)
    entities = Column(JSON, nullable=True)
    sentiment = Column(String, nullable=True)
    response_time = Column(Float, nullable=True)  # in seconds
    created_at = Column(DateTime, default=datetime.datetime.utcnow)


class KnowledgeBase(Base):
    __tablename__ = "knowledge_base"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    category = Column(String, nullable=False)  # 'regulation', 'practice', 'faq'
    language = Column(String, default="en")
    source = Column(String, nullable=True)  # e.g., 'Bank of Tanzania', 'TRA'
    relevance_score = Column(Float, default=1.0)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    meta_data = Column(JSON, nullable=True)
