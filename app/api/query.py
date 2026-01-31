from fastapi import APIRouter, HTTPException
from app.models.schemas import QueryRequest, QueryResponse
from app.services.parser import ParseError, parse_question
from app.services.price_store import PriceStore


router = APIRouter()

price_store = PriceStore("/app/data/stock_prices.csv")

@router.post("/query", response_model=QueryResponse)
def query_price(request: QueryRequest):
    try:
        parsed = parse_question(request.question)
    except ParseError as e:
        raise HTTPException(status_code=400, detail=str(e))

    result = price_store.find_price(**parsed)

    if not result:
        raise HTTPException(status_code=404, detail="Price not found")

    return QueryResponse(**result)

    
    