from pathlib import Path
import pandas as pd

# ============================================================
# Paths
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_PATH = PROJECT_ROOT / "data" / "raw"
SUPPORTING_PATH = PROJECT_ROOT / "data" / "supporting"

# ============================================================
# File Lists
# ============================================================

CORE_FILES = [
    "analysis.xlsx",
    "balancesheet.xlsx",
    "cashflow.xlsx",
    "companies.xlsx",
    "documents.xlsx",
    "profitandloss.xlsx",
    "prosandcons.xlsx"
]

SUPPLEMENTARY_FILES = [
    "financial_ratios.xlsx",
    "market_cap.xlsx",
    "peer_groups.xlsx",
    "sectors.xlsx",
    "stock_prices.xlsx"
]

# ============================================================
# Helper
# ============================================================

def normalize_company_id(df):
    if "company_id" in df.columns:
        df["company_id"] = (
            df["company_id"]
            .astype(str)
            .str.strip()
            .str.upper()
        )

    if "id" in df.columns and "company_name" in df.columns:
        df["id"] = (
            df["id"]
            .astype(str)
            .str.strip()
            .str.upper()
        )

    return df

# ============================================================
# Core Files
# ============================================================

for file_name in CORE_FILES:

    file_path = RAW_PATH / file_name

    print("\n" + "=" * 60)
    print(f"FILE: {file_name}")
    print("=" * 60)

    excel_file = pd.ExcelFile(file_path)

    print(f"Sheets Found: {len(excel_file.sheet_names)}")

    for sheet in excel_file.sheet_names:

        df = pd.read_excel(
            file_path,
            sheet_name=sheet,
            header=1
        )

        df = normalize_company_id(df)

        print(
            f"{sheet:<30}"
            f"Rows: {df.shape[0]:<8}"
            f"Cols: {df.shape[1]}"
        )

# ============================================================
# Supplementary Files
# ============================================================

for file_name in SUPPLEMENTARY_FILES:

    file_path = SUPPORTING_PATH / file_name

    print("\n" + "=" * 60)
    print(f"FILE: {file_name}")
    print("=" * 60)

    excel_file = pd.ExcelFile(file_path)

    print(f"Sheets Found: {len(excel_file.sheet_names)}")

    for sheet in excel_file.sheet_names:

        df = pd.read_excel(
            file_path,
            sheet_name=sheet,
            header=0
        )

        df = normalize_company_id(df)

        print(
            f"{sheet:<30}"
            f"Rows: {df.shape[0]:<8}"
            f"Cols: {df.shape[1]}"
        )