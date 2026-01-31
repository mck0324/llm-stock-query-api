from pydantic import BaseModel

class QueryResponse(BaseModel):
    market: str
    symbol: str
    name: str
    date: str
    price_type: str
    value: float

class QueryRequest(BaseModel):
    question: str