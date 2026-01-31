import csv
from pathlib import Path
from typing import Any, Dict, Optional


class PriceStore:
    def __init__(self, csv_path: str):
        self.csv_path = Path(csv_path)
        self.rows = self._load()

    def _load(self) -> list[Dict[str, Any]]:
        if not self.csv_path.exists():
            raise FileNotFoundError(f"CSV not found: {self.csv_path}")
        
        with self.csv_path.open(newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            rows = []
            for row in reader:
                rows.append({
                    "date": row["date"],
                    "market": row["market"],
                    "symbol": row["symbol"],
                    "name": row["name"],
                    "open": float(row["open"]),
                    "high": float(row["high"]),
                    "low": float(row["low"]),
                    "close": float(row["close"])
                })
            return rows


    def find_price(
        self,
        *,
        market: str,
        symbol: str,
        date: str,
        price_type: str
    ) -> Optional[Dict[str, Any]]:
        for row in self.rows:
            if (
                row["market"] == market
                and row["symbol"] == symbol
                and row["date"] == date
            ):
                return {
                    "market": market,
                    "symbol": symbol,
                    "name": row["name"],
                    "date": date,
                    "price_type": price_type,
                    "value": row[price_type],
                }
        return None