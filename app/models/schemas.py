from pydantic import BaseModel

class QueryResponse(BaseModel):
    question: str

class QueryRequest(BaseModel):
    market: str
    symbol: str
    name: str
    date: str
    price_type: str
    value: float