from datetime import timedelta

from app.db.models import AsyncSessionLocal
from app.schemas.user import UserCreate, UserLogin, UserProfile
from app.services import auth as auth_service
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


def get_db():
    db = AsyncSessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register", response_model=UserProfile)
async def register_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    existing = await auth_service.get_user_by_email(db, user.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    user_dict = user.dict()
    user_dict["password"] = user.password
    new_user = await auth_service.create_user(db, user_dict)
    profile_data = {
        k: v
        for k, v in new_user.__dict__.items()
        if not k.startswith("_") and k != "hashed_password"
    }
    profile_data["created_at"] = str(new_user.created_at)
    return UserProfile(**profile_data)


@router.post("/login")
async def login_user(user: UserLogin, db: AsyncSession = Depends(get_db)):
    db_user = await auth_service.get_user_by_email(db, user.email)
    if not db_user or not auth_service.verify_password(
        user.password, db_user.hashed_password
    ):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = auth_service.create_access_token(
        {"sub": db_user.email},
        timedelta(minutes=auth_service.ACCESS_TOKEN_EXPIRE_MINUTES),
    )
    return {"access_token": token, "token_type": "bearer"}


@router.get("/profile")
async def get_profile():
    """Get current user profile."""
    pass


@router.put("/profile")
async def update_profile():
    """Update user profile."""
    pass
