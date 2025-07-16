from typing import Optional

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: Optional[str]
    phone_number: Optional[str]
    age_group: Optional[str]
    gender: Optional[str]
    location: Optional[str]
    language: Optional[str] = 'en'

    model_config = {
        "extra": "forbid"
    }


class UserLogin(BaseModel):
    email: EmailStr
    password: str

    model_config = {
        "extra": "forbid"
    }


class UserProfile(BaseModel):
    id: int
    email: EmailStr
    full_name: Optional[str]
    phone_number: Optional[str]
    age_group: Optional[str]
    gender: Optional[str]
    location: Optional[str]
    language: str
    created_at: str

    model_config = {
        "extra": "forbid"
    }
