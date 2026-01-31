# llm-stock-query-api

flow
Client
  │
  │  Natural language question
  ▼
Backend API (FastAPI)
  │
  │  1. Parse natural language → structured query
  ▼
LLM (OpenAI)
  │
  │  JSON only (market, symbol, date, price_type)
  ▼
Backend API
  │
  │  2. Query trusted data source
  ▼
CSV (Price Store)
  │
  │  Exact match result
  ▼
Backend API
  │
  │  Build response
  ▼
Client
