from app.core.cache import get_expensive_data
from app.core.rate_limit import rate_limit
from app.db.models import User
from app.db.session import get_db
from app.schemas.finance import (
    BudgetCreate, ExpenseCreate, IncomeSourceCreate, IncomeSourceResponse,
    SavingsGoalCreate
)
from app.schemas.finance import (
    ExpenseCreate, BudgetCreate, SavingsGoalCreate
)
from app.services import finance as finance_service
from app.tasks.background import process_heavy_calculation
from fastapi import APIRouter, BackgroundTasks, Depends, Header, HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.services.auth import decode_access_token

router = APIRouter()
security = HTTPBearer()

async def get_user_id_from_token(credentials: HTTPAuthorizationCredentials = Security(security), db: AsyncSession = Depends(get_db)) -> int:
    token = credentials.credentials
    payload = decode_access_token(token)
    if not payload or "sub" not in payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    
    # Look up user_id from database using email
    email = payload["sub"]
    result = await db.execute(select(User.id).where(User.email == email))
    user_id = result.scalar()
    
    if not user_id:
        raise HTTPException(status_code=401, detail="User not found")
    
    return user_id

@router.post("/income-sources", response_model=IncomeSourceResponse, dependencies=[Depends(rate_limit)])
async def add_income_source(
    data: IncomeSourceCreate,
    db: AsyncSession = Depends(get_db),
    user_id: int = Depends(get_user_id_from_token)
):
    income = await finance_service.create_income_source(db, user_id, data.model_dump())
    return income

@router.get("/income-sources", response_model=list[IncomeSourceResponse], dependencies=[Depends(rate_limit)])
async def list_income_sources(
    db: AsyncSession = Depends(get_db),
    user_id: int = Depends(get_user_id_from_token)
):
    return await finance_service.list_income_sources(db, user_id)

# EXPENSES CRUD
@router.post("/expenses", dependencies=[Depends(rate_limit)])
async def add_expense(
    data: ExpenseCreate,
    db: AsyncSession = Depends(get_db),
    user_id: int = Depends(get_user_id_from_token)
):
    expense = await finance_service.create_expense(db, user_id, data.model_dump())
    return expense

@router.get("/expenses", dependencies=[Depends(rate_limit)])
async def list_expenses(
    db: AsyncSession = Depends(get_db),
    user_id: int = Depends(get_user_id_from_token)
):
    return await finance_service.list_expenses(db, user_id)

@router.put("/expenses/{expense_id}", dependencies=[Depends(rate_limit)])
async def update_expense(
    expense_id: int,
    data: ExpenseCreate,
    db: AsyncSession = Depends(get_db),
    user_id: int = Depends(get_user_id_from_token)
):
    updated = await finance_service.update_expense(db, user_id, expense_id, data.model_dump())
    if not updated:
        raise HTTPException(status_code=404, detail="Expense not found")
    return updated

@router.delete("/expenses/{expense_id}", dependencies=[Depends(rate_limit)])
async def delete_expense(
    expense_id: int,
    db: AsyncSession = Depends(get_db),
    user_id: int = Depends(get_user_id_from_token)
):
    deleted = await finance_service.delete_expense(db, user_id, expense_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Expense not found")
    return {"message": "Expense deleted"}

# BUDGETS CRUD
@router.post("/budgets", dependencies=[Depends(rate_limit)])
async def add_budget(
    data: BudgetCreate,
    db: AsyncSession = Depends(get_db),
    user_id: int = Depends(get_user_id_from_token)
):
    budget = await finance_service.create_budget(db, user_id, data.model_dump())
    return budget

@router.get("/budgets", dependencies=[Depends(rate_limit)])
async def list_budgets(
    db: AsyncSession = Depends(get_db),
    user_id: int = Depends(get_user_id_from_token)
):
    return await finance_service.list_budgets(db, user_id)

@router.put("/budgets/{budget_id}", dependencies=[Depends(rate_limit)])
async def update_budget(
    budget_id: int,
    data: BudgetCreate,
    db: AsyncSession = Depends(get_db),
    user_id: int = Depends(get_user_id_from_token)
):
    updated = await finance_service.update_budget(db, user_id, budget_id, data.model_dump())
    if not updated:
        raise HTTPException(status_code=404, detail="Budget not found")
    return updated

@router.delete("/budgets/{budget_id}", dependencies=[Depends(rate_limit)])
async def delete_budget(
    budget_id: int,
    db: AsyncSession = Depends(get_db),
    user_id: int = Depends(get_user_id_from_token)
):
    deleted = await finance_service.delete_budget(db, user_id, budget_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Budget not found")
    return {"message": "Budget deleted"}

# SAVINGS GOALS CRUD
@router.post("/savings-goals", dependencies=[Depends(rate_limit)])
async def add_savings_goal(
    data: SavingsGoalCreate,
    db: AsyncSession = Depends(get_db),
    user_id: int = Depends(get_user_id_from_token)
):
    goal = await finance_service.create_savings_goal(db, user_id, data.model_dump())
    return goal

@router.get("/savings-goals", dependencies=[Depends(rate_limit)])
async def list_savings_goals(
    db: AsyncSession = Depends(get_db),
    user_id: int = Depends(get_user_id_from_token)
):
    return await finance_service.list_savings_goals(db, user_id)

@router.put("/savings-goals/{goal_id}", dependencies=[Depends(rate_limit)])
async def update_savings_goal(
    goal_id: int,
    data: SavingsGoalCreate,
    db: AsyncSession = Depends(get_db),
    user_id: int = Depends(get_user_id_from_token)
):
    updated = await finance_service.update_savings_goal(db, user_id, goal_id, data.model_dump())
    if not updated:
        raise HTTPException(status_code=404, detail="Savings goal not found")
    return updated

@router.delete("/savings-goals/{goal_id}", dependencies=[Depends(rate_limit)])
async def delete_savings_goal(
    goal_id: int,
    db: AsyncSession = Depends(get_db),
    user_id: int = Depends(get_user_id_from_token)
):
    deleted = await finance_service.delete_savings_goal(db, user_id, goal_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Savings goal not found")
    return {"message": "Savings goal deleted"}

# Real-time analytics endpoint (scaffold)
@router.get("/income-sources/stream", dependencies=[Depends(rate_limit)])
async def stream_income_sources(user_id: int = Depends(get_user_id_from_token)):
    # This is a placeholder for a real-time streaming endpoint
    # In production, use WebSockets or Server-Sent Events (SSE)
    # and supabase.realtime.subscribe to push updates to the client
    return {"message": "Real-time streaming not yet implemented. Use Supabase client for live updates."}
