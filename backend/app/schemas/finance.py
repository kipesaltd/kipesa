from typing import Optional

from pydantic import BaseModel


class ExpenseCreate(BaseModel):
    amount: float
    category: str
    description: Optional[str]
    date: str

    model_config = {
        "extra": "forbid"
    }


class BudgetCreate(BaseModel):
    amount: float
    category: str
    period: str  # e.g., 'monthly', 'yearly'

    model_config = {
        "extra": "forbid"
    }


class SavingsGoalCreate(BaseModel):
    target_amount: float
    description: Optional[str]
    target_date: str

    model_config = {
        "extra": "forbid"
    }


class IncomeSourceCreate(BaseModel):
    name: str
    amount: float
    frequency: Optional[str]
    description: Optional[str]

    model_config = {
        "extra": "forbid"
    }


class IncomeSourceResponse(BaseModel):
    id: int
    user_id: int
    name: str
    amount: float
    frequency: Optional[str]
    description: Optional[str]
    created_at: str

    model_config = {
        "extra": "forbid"
    }
