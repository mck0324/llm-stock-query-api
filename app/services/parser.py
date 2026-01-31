import json
from typing import Any, Dict
from openai import OpenAI

client= OpenAI()

SYSTEM_PROMPT = """
너는 금융 질문을 구조화된 JSON으로 변환하는 파서다.
너의 출력은 다른 프로그램에서 바로 json.loads()로 파싱된다.

[출력 규칙]
- 응답은 반드시 JSON 객체만 출력해라
- ``` 또는 마크다운 문법을 절대 사용하지 마라
- 설명, 주석, 문장, 공백 텍스트를 절대 포함하지 마라

[출력 스키마]
아래 JSON 스키마를 반드시 지켜라.
다른 필드는 절대 포함하지 마라.

{
  "market": "KOSPI | KOSDAQ | NASDAQ",
  "symbol": "종목 코드 또는 티커",
  "date": "YYYY-MM-DD",
  "price_type": "open | close | high | low"
}

[규칙]
- 가격 값(value)은 절대 생성하지 마라
- 스키마에 없는 필드는 절대 추가하지 마라
- 판단 불가한 필드는 반드시 null로 설정해라
- 날짜는 반드시 YYYY-MM-DD 형식으로 반환해라
"""

class ParseError(Exception):
    pass

def parse_question(question: str) -> Dict[str, Any]:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question},
        ],
        temperature=0,
    )
    content = response.choices[0].message.content.strip()

    try:
        content = response.choices[0].message.content
        content = clean_llm_json(content)
        parsed = json.loads(content)
    except json.JSONDecodeError:
        raise ParseError(f"Invalid JSON from LLM: {content}")

    required_fields = ["market", "symbol", "date", "price_type"]
    for field in required_fields:
        if field not in parsed or parsed[field] is None:
            raise ParseError(f"Missing field: {field}")

    return parsed

def clean_llm_json(content: str) -> str:
    content = content.strip()

    if content.startswith("```"):
        content = content.split("```")[1]

    return content.strip()