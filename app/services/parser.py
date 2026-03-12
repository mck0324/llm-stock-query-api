import json
from typing import Any, Dict, TypedDict
from openai import OpenAI

from app.services.llm_service import LLMService

client= OpenAI()



class ParseError(Exception):
    pass

class PaserQuestion(TypedDict):
    market: str
    symbol: str
    date: str
    price_type: str

SYSTEM_PROMPT = """
You convert a stock price question into JSON.
Return JSON only with:
- market
- symbol
- date
- price_type

Allowed price_type values:
open, high, low, close
""".strip()


def parse_question(question: str) -> PaserQuestion:
    llm = LLMService()
    raw = llm.chat_json(SYSTEM_PROMPT, user_prompt=question,)
    
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError:
        raise ParseError(f"Invalid JSON from LLM: {raw}") from exec

    required = {"market", "symbol", "date", "price_type"}
    missing = required - set(parsed.keys())
    if missing:
        raise ParseError(f"Missing fields: {sorted(missing)}")

    return {
        "market": parsed["market"],
        "symbol": parsed["symbol"],
        "date": parsed["date"],
        "price_type": parsed["price_type"],
    }


    return PaserQuestion(**parsed)