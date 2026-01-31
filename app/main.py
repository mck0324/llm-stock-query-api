from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from app.api.query import router as query_router

app = FastAPI(
    title="Stock Price Q&A API",
    version="0.1.0",
)


app.include_router(query_router, prefix="/api")


@app.get("/health")
def health():
    return {"status": "ok"}
