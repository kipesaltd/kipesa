from datetime import datetime, timedelta

from app.core.config import get_settings
from app.db.models import User
from app.db.supabase import supabase
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

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
    # Register user in Supabase Auth
    auth_resp = supabase.auth.sign_up({
        "email": user_data["email"],
        "password": user_data["password"]
    })
    if not auth_resp or not auth_resp.user:
        raise Exception("Supabase Auth registration failed")
    # Sync user to local DB
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


def supabase_login(email: str, password: str):
    auth_resp = supabase.auth.sign_in_with_password({
        "email": email,
        "password": password
    })
    if not auth_resp or not auth_resp.session:
        return None
    return auth_resp


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
    except JWTError:
        return None

def get_supabase_user(access_token: str):
    resp = supabase.auth.get_user(access_token)
    if not resp or not resp.user:
        return None
    return resp.user

def update_supabase_user(access_token: str, update_data: dict):
    resp = supabase.auth.update_user(access_token, attributes=update_data)
    if not resp or not resp.user:
        return None
    return resp.user

def change_supabase_password(access_token: str, new_password: str):
    resp = supabase.auth.update_user(access_token, attributes={"password": new_password})
    if not resp or not resp.user:
        return None
    return resp.user

def send_supabase_password_reset(email: str):
    resp = supabase.auth.reset_password_for_email(email)
    return resp
