from fastapi import APIRouter
from app.models.schemas import QueryRequest, QueryResponse


router = APIRouter()

@router.post("/query", response_model=QueryResponse)
def query_price(request: QueryRequest):
    # temporary mock data
    return QueryResponse(
        market="KOSPI",
        symbol="005930",
        name="삼성전자",
        date="2025-01-29",
        price_type="close",
        value=72000
    )
    