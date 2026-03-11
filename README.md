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


위에는 초기 간단한 FASTAPI 기반 생성형 AI를 만들어봤고 이제 좀 더 깊숙히 들어가보자 한다!

플랜

FastAPI 기반 생성형 AI 백엔드

LangGraph 기반 질의 라우팅 Agent

LlamaIndex 기반 RAG 구축

문서 ingestion / chunking / embedding 파이프라인

하이브리드 검색 초안

synthetic QA dataset 생성

선택적으로 MCP server 초안