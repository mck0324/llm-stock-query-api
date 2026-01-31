from fastapi import APIRouter, HTTPException
from app.models.schemas import QueryRequest, QueryResponse
from app.services.price_store import PriceStore


router = APIRouter()

price_store = PriceStore("/app/data/stock_prices.csv")

@router.post("/query", response_model=QueryResponse)
def query_price(request: QueryRequest):
    # temporary mock data
    parsed = {
        "market": "KOSPI",
        "symbol": "005930",
        "date": "2025-01-29",
        "price_type": "close",
    }

    result = price_store.find_price(**parsed)

    if not result:
        raise HTTPException(status_code=404, detail="Price not found")

    return QueryResponse(**result)

    
    