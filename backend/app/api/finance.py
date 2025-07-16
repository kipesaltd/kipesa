from app.core.cache import get_expensive_data
from app.core.rate_limit import rate_limit
from app.db.models import (AsyncSessionLocal, Budget, Expense, IncomeSource,
                           SavingsGoal)
from app.schemas.finance import (BudgetCreate, ExpenseCreate,
                                 IncomeSourceCreate, IncomeSourceResponse,
                                 SavingsGoalCreate)
from app.tasks.background import process_heavy_calculation
from fastapi import APIRouter, BackgroundTasks, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

router = APIRouter()


async def get_db():
    db = AsyncSessionLocal()
    try:
        yield db
    finally:
        await db.close()


@router.post(
    "/income-sources",
    response_model=IncomeSourceResponse,
    dependencies=[Depends(rate_limit)],
)
async def add_income_source(
    data: IncomeSourceCreate, db: AsyncSession = Depends(get_db)
):
    income = IncomeSource(**data.dict())
    db.add(income)
    await db.commit()
    await db.refresh(income)
    return income


@router.get(
    "/income-sources",
    response_model=list[IncomeSourceResponse],
    dependencies=[Depends(rate_limit)],
)
async def list_income_sources(db: AsyncSession = Depends(get_db)):
    # Example: cache the result for 60 seconds
    cache_key = "income_sources"
    cached_result = await get_expensive_data(cache_key)
    if cached_result:
        return cached_result
    result = await db.execute(select(IncomeSource))
    data = result.scalars().all()
    # Optionally, set cache here if not using decorator directly
    return data


@router.post("/expenses", dependencies=[Depends(rate_limit)])
async def add_expense(data: ExpenseCreate, db: AsyncSession = Depends(get_db)):
    expense = Expense(**data.dict())
    db.add(expense)
    await db.commit()
    await db.refresh(expense)
    return expense


@router.get("/expenses", dependencies=[Depends(rate_limit)])
async def list_expenses(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Expense))
    return result.scalars().all()


@router.post("/budgets", dependencies=[Depends(rate_limit)])
async def add_budget(data: BudgetCreate, db: AsyncSession = Depends(get_db)):
    budget = Budget(**data.dict())
    db.add(budget)
    await db.commit()
    await db.refresh(budget)
    return budget


@router.get("/budgets", dependencies=[Depends(rate_limit)])
async def list_budgets(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Budget))
    return result.scalars().all()


@router.post("/savings-goals", dependencies=[Depends(rate_limit)])
async def add_savings_goal(data: SavingsGoalCreate, db: AsyncSession = Depends(get_db)):
    goal = SavingsGoal(**data.dict())
    db.add(goal)
    await db.commit()
    await db.refresh(goal)
    return goal


@router.get("/savings-goals", dependencies=[Depends(rate_limit)])
async def list_savings_goals(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(SavingsGoal))
    return result.scalars().all()


@router.post(
    "/trigger-background-task",
    dependencies=[Depends(rate_limit)]
)
async def trigger_background_task(
    user_id: int, background_tasks: BackgroundTasks
):
    background_tasks.add_task(
        process_heavy_calculation, {"user_id": user_id}
    )
    return {
        "message": "Background task started"
    }
