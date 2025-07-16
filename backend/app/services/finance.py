from app.db.models import IncomeSource, Expense, Budget, SavingsGoal
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

# INCOME SOURCES
async def create_income_source(session: AsyncSession, user_id: int, data: dict):
    income = IncomeSource(user_id=user_id, **data)
    session.add(income)
    await session.commit()
    await session.refresh(income)
    return income

async def list_income_sources(session: AsyncSession, user_id: int):
    result = await session.execute(select(IncomeSource).where(IncomeSource.user_id == user_id))
    return result.scalars().all()

async def update_income_source(session: AsyncSession, user_id: int, income_id: int, data: dict):
    result = await session.execute(select(IncomeSource).where(IncomeSource.id == income_id, IncomeSource.user_id == user_id))
    income = result.scalars().first()
    if not income:
        return None
    for k, v in data.items():
        setattr(income, k, v)
    await session.commit()
    await session.refresh(income)
    return income

async def delete_income_source(session: AsyncSession, user_id: int, income_id: int):
    result = await session.execute(select(IncomeSource).where(IncomeSource.id == income_id, IncomeSource.user_id == user_id))
    income = result.scalars().first()
    if not income:
        return False
    await session.delete(income)
    await session.commit()
    return True

# EXPENSES
async def create_expense(session: AsyncSession, user_id: int, data: dict):
    expense = Expense(user_id=user_id, **data)
    session.add(expense)
    await session.commit()
    await session.refresh(expense)
    return expense

async def list_expenses(session: AsyncSession, user_id: int):
    result = await session.execute(select(Expense).where(Expense.user_id == user_id))
    return result.scalars().all()

async def update_expense(session: AsyncSession, user_id: int, expense_id: int, data: dict):
    result = await session.execute(select(Expense).where(Expense.id == expense_id, Expense.user_id == user_id))
    expense = result.scalars().first()
    if not expense:
        return None
    for k, v in data.items():
        setattr(expense, k, v)
    await session.commit()
    await session.refresh(expense)
    return expense

async def delete_expense(session: AsyncSession, user_id: int, expense_id: int):
    result = await session.execute(select(Expense).where(Expense.id == expense_id, Expense.user_id == user_id))
    expense = result.scalars().first()
    if not expense:
        return False
    await session.delete(expense)
    await session.commit()
    return True

# BUDGETS
async def create_budget(session: AsyncSession, user_id: int, data: dict):
    budget = Budget(user_id=user_id, **data)
    session.add(budget)
    await session.commit()
    await session.refresh(budget)
    return budget

async def list_budgets(session: AsyncSession, user_id: int):
    result = await session.execute(select(Budget).where(Budget.user_id == user_id))
    return result.scalars().all()

async def update_budget(session: AsyncSession, user_id: int, budget_id: int, data: dict):
    result = await session.execute(select(Budget).where(Budget.id == budget_id, Budget.user_id == user_id))
    budget = result.scalars().first()
    if not budget:
        return None
    for k, v in data.items():
        setattr(budget, k, v)
    await session.commit()
    await session.refresh(budget)
    return budget

async def delete_budget(session: AsyncSession, user_id: int, budget_id: int):
    result = await session.execute(select(Budget).where(Budget.id == budget_id, Budget.user_id == user_id))
    budget = result.scalars().first()
    if not budget:
        return False
    await session.delete(budget)
    await session.commit()
    return True

# SAVINGS GOALS
async def create_savings_goal(session: AsyncSession, user_id: int, data: dict):
    goal = SavingsGoal(user_id=user_id, **data)
    session.add(goal)
    await session.commit()
    await session.refresh(goal)
    return goal

async def list_savings_goals(session: AsyncSession, user_id: int):
    result = await session.execute(select(SavingsGoal).where(SavingsGoal.user_id == user_id))
    return result.scalars().all()

async def update_savings_goal(session: AsyncSession, user_id: int, goal_id: int, data: dict):
    result = await session.execute(select(SavingsGoal).where(SavingsGoal.id == goal_id, SavingsGoal.user_id == user_id))
    goal = result.scalars().first()
    if not goal:
        return None
    for k, v in data.items():
        setattr(goal, k, v)
    await session.commit()
    await session.refresh(goal)
    return goal

async def delete_savings_goal(session: AsyncSession, user_id: int, goal_id: int):
    result = await session.execute(select(SavingsGoal).where(SavingsGoal.id == goal_id, SavingsGoal.user_id == user_id))
    goal = result.scalars().first()
    if not goal:
        return False
    await session.delete(goal)
    await session.commit()
    return True 