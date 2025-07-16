from typing import Optional

from pydantic import BaseModel


class ContentCreate(BaseModel):
    title: str
    body: str
    language: str
    author: Optional[str]
    tags: Optional[list[str]]

    model_config = {
        "extra": "forbid"
    }


class ContentResponse(BaseModel):
    id: int
    title: str
    body: str
    language: str
    author: Optional[str]
    tags: Optional[list[str]]
    created_at: str

    model_config = {
        "extra": "forbid"
    }
