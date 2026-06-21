import sqlite3
import pandas as pd
from pathlib import Path

from src.etl.loader import load_core_excel

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DB_FILE = PROJECT_ROOT / "data" / "nifty100.db"

SCHEMA_FILE = PROJECT_ROOT / "db" / "schema.sql"

SUPPORTING_DIR = PROJECT_ROOT / "data" / "supporting"

CORE_FILES = {
    "companies.xlsx": "companies",
    "profitandloss.xlsx": "profitandloss",
    "balancesheet.xlsx": "balancesheet",
    "cashflow.xlsx": "cashflow",
    "analysis.xlsx": "analysis",
    "documents.xlsx": "documents",
    "prosandcons.xlsx": "prosandcons"
}

SUPPORTING_FILES = {
    "sectors.xlsx": "sectors",
    "market_cap.xlsx": "market_cap",
    "stock_prices.xlsx": "stock_prices",
    "financial_ratios.xlsx": "financial_ratios",
    "peer_groups.xlsx": "peer_groups"
}

if DB_FILE.exists():
    DB_FILE.unlink()

conn = sqlite3.connect(DB_FILE)

with open(SCHEMA_FILE, "r") as f:
    conn.executescript(f.read())

print("Database Created")

for file_name, table_name in CORE_FILES.items():

    df = load_core_excel(file_name)

    df.to_sql(
        table_name,
        conn,
        if_exists="append",
        index=False
    )

    print(
        f"{table_name} -> {len(df)} rows"
    )

for file_name, table_name in SUPPORTING_FILES.items():

    file_path = (
        SUPPORTING_DIR / file_name
    )

    df = pd.read_excel(
        file_path
    )

    df.to_sql(
        table_name,
        conn,
        if_exists="append",
        index=False
    )

    print(
        f"{table_name} -> {len(df)} rows"
    )

conn.commit()

conn.close()

print("\nLoad Complete")
print(DB_FILE)