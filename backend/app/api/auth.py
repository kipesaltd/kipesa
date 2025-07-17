from datetime import timedelta

from app.db.session import get_db
from app.schemas.user import UserCreate, UserLogin, UserProfile
from app.services import auth as auth_service
from fastapi import APIRouter, Depends, HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()
security = HTTPBearer()  # Standard HTTPBearer for protected endpoints

@router.post("/register", response_model=UserProfile)
async def register_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    """Register a new user. No authentication required."""
    existing = await auth_service.get_user_by_email(db, user.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    user_dict = user.model_dump()
    user_dict["password"] = user.password
    new_user = await auth_service.create_user_supabase_and_local(db, user_dict)
    profile_data = {
        k: v
        for k, v in new_user.__dict__.items()
        if not k.startswith("_") and k != "hashed_password"
    }
    profile_data["created_at"] = str(new_user.created_at)
    return UserProfile(**profile_data)


@router.post("/login")
async def login_user(user: UserLogin):
    """Login user and get access token. No authentication required."""
    auth_resp = auth_service.supabase_login(user.email, user.password)
    if not auth_resp:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = auth_service.create_access_token(
        {"sub": user.email},
        timedelta(minutes=auth_service.ACCESS_TOKEN_EXPIRE_MINUTES),
    )
    return {"access_token": token, "token_type": "bearer"}


@router.get("/profile", dependencies=[Depends(security)])
async def get_profile(credentials: HTTPAuthorizationCredentials = Security(security)):
    """Get user profile. Authentication required."""
    access_token = credentials.credentials
    user = auth_service.get_supabase_user(access_token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return user

@router.put("/profile", dependencies=[Depends(security)])
async def update_profile(update_data: dict, credentials: HTTPAuthorizationCredentials = Security(security)):
    """Update user profile. Authentication required."""
    access_token = credentials.credentials
    user = auth_service.update_supabase_user(access_token, update_data)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return user

@router.post("/change-password", dependencies=[Depends(security)])
async def change_password(new_password: str, credentials: HTTPAuthorizationCredentials = Security(security)):
    """Change user password. Authentication required."""
    access_token = credentials.credentials
    user = auth_service.change_supabase_password(access_token, new_password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return {"message": "Password updated"}

@router.post("/send-password-reset")
async def send_password_reset(email: str):
    """Send password reset email. No authentication required."""
    resp = auth_service.send_supabase_password_reset(email)
    if not resp:
        raise HTTPException(status_code=400, detail="Failed to send password reset email")
    return {"message": "Password reset email sent"}
