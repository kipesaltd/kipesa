from fastapi import APIRouter

router = APIRouter()


@router.post("/loan")
async def loan_calculator():
    """Calculate loan details."""
    pass


@router.post("/savings")
async def savings_calculator():
    """Calculate savings projection."""
    pass


@router.post("/tax")
async def tax_calculator():
    """Calculate tax details."""
    pass


@router.post("/business")
async def business_planning_calculator():
    """Business planning calculator."""
    pass
