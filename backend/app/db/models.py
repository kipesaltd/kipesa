import datetime

from app.core.config import get_settings
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.ext.asyncio import (AsyncAttrs, async_sessionmaker,
                                    create_async_engine)
from sqlalchemy.orm import declarative_base
from sqlalchemy.pool import NullPool

settings = get_settings()

DATABASE_URL = settings.DATABASE_URL

# Configure engine with valid connection pool settings
engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    future=True,
    pool_pre_ping=True,  # Verify connections before use
    pool_recycle=3600,   # Recycle connections after 1 hour
    poolclass=NullPool if "supabase" in DATABASE_URL.lower() else None
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
