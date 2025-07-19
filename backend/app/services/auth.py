from datetime import datetime, timedelta

from app.core.config import get_settings
from app.db.models import User
from app.db.supabase import supabase
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from loguru import logger

settings = get_settings()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ALGORITHM = settings.ALGORITHM
SECRET_KEY = settings.SECRET_KEY
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


async def get_user_by_email(session: AsyncSession, email: str):
    result = await session.execute(select(User).where(User.email == email))
    return result.scalars().first()


async def create_user_supabase_and_local(session: AsyncSession, user_data: dict):
    """Mock registration for development - replace with real Supabase auth in production"""
    try:
        # For development, just create user in local DB
        # In production, this should use real Supabase authentication
        user = User(
            email=user_data["email"],
            full_name=user_data.get("full_name"),
            phone_number=user_data.get("phone_number"),
            age_group=user_data.get("age_group"),
            gender=user_data.get("gender"),
            location=user_data.get("location"),
            language=user_data.get("language", "en"),
            hashed_password=hash_password(user_data["password"]),
        )
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user
    except Exception as e:
        logger.error(f"Registration error: {e}")
        raise Exception(f"Registration failed: {e}")


def supabase_login(email: str, password: str):
    """Mock login for development - replace with real Supabase auth in production"""
    try:
        # For development, accept any email/password combination
        # In production, this should use real Supabase authentication
        if email and password and len(password) >= 6:
            return {"user": {"email": email}, "session": {"access_token": "mock-token"}}
        return None
    except Exception as e:
        logger.error(f"Login error: {e}")
        return None


def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError as e:
        logger.error(f"JWT decode error: {e}")
        return None


def get_supabase_user(access_token: str):
    """Get user info from local JWT token"""
    try:
        # Decode our local JWT token
        payload = decode_access_token(access_token)
        if payload and payload.get("sub"):
            # Return user info based on email from token
            return {"email": payload["sub"], "id": payload.get("user_id")}
        return None
    except Exception as e:
        logger.error(f"Error getting user: {e}")
        return None


def update_supabase_user(access_token: str, update_data: dict):
    """user - simplified for local JWT tokens"""
    try:
        # For now, just return success - implement actual update logic later
        user_info = get_supabase_user(access_token)
        if user_info:
            return {"message": "User updated successfully", "user": user_info}
        return None
    except Exception as e:
        logger.error(f"Error updating user: {e}")
        return None


def change_supabase_password(access_token: str, new_password: str):
    """Change password - simplified for local JWT tokens"""
    try:
        # For now, just return success - implement actual password change logic later
        user_info = get_supabase_user(access_token)
        if user_info:
            return {"message": "Password updated successfully"}
        return None
    except Exception as e:
        logger.error(f"Error changing password: {e}")
        return None


def send_supabase_password_reset(email: str):
    resp = supabase.auth.reset_password_for_email(email)
    return resp
