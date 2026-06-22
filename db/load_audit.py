import sqlite3
import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DB_PATH = PROJECT_ROOT / "data" / "nifty100.db"
OUTPUT_FILE = PROJECT_ROOT / "reports" / "load_audit.csv"

conn = sqlite3.connect(DB_PATH)

tables = [
    "companies",
    "profitandloss",
    "balancesheet",
    "cashflow",
    "analysis",
    "documents",
    "prosandcons",
    "sectors",
    "market_cap",
    "stock_prices",
    "financial_ratios",
    "peer_groups"
]

audit_rows = []

for table in tables:

    count = pd.read_sql_query(
        f"SELECT COUNT(*) AS row_count FROM {table}",
        conn
    )

    audit_rows.append({
        "table_name": table,
        "row_count": int(count.iloc[0]["row_count"])
    })

audit_df = pd.DataFrame(audit_rows)

audit_df.to_csv(

    OUTPUT_FILE,

    index=False

)

print(audit_df)

print("\nSaved:")
print(OUTPUT_FILE)

conn.close()