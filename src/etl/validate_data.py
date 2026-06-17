from pathlib import Path
import pandas as pd

# ============================================================
# Paths
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_PATH = PROJECT_ROOT / "data" / "raw"
SUPPORTING_PATH = PROJECT_ROOT / "data" / "supporting"

# ============================================================
# Files
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


def validate_dataset(df):

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("\nFirst 5 Rows:")
    print(df.head())

    # ========================================================
    # Primary Key Checks
    # ========================================================

    print("\nPrimary Key Checks:")

    if "company_name" in df.columns and "id" in df.columns:

        duplicates = df["id"].duplicated().sum()

        print(f"Company ID duplicates: {duplicates}")

    elif (
        "company_id" in df.columns
        and "year" in df.columns
    ):

        duplicates = (
            df.duplicated(
                subset=["company_id", "year"]
            )
            .sum()
        )

        print(
            f"(company_id, year) duplicates: "
            f"{duplicates}"
        )

# ============================================================
# Core Files Validation
# ============================================================

for file_name in CORE_FILES:

    file_path = RAW_PATH / file_name

    excel_file = pd.ExcelFile(file_path)

    print("\n" + "=" * 80)
    print(f"FILE: {file_name}")
    print("=" * 80)

    for sheet in excel_file.sheet_names:

        print(f"\nSheet: {sheet}")

        df = pd.read_excel(
            file_path,
            sheet_name=sheet,
            header=1
        )

        df = normalize_company_id(df)

        validate_dataset(df)

# ============================================================
# Supplementary Files Validation
# ============================================================

for file_name in SUPPLEMENTARY_FILES:

    file_path = SUPPORTING_PATH / file_name

    excel_file = pd.ExcelFile(file_path)

    print("\n" + "=" * 80)
    print(f"FILE: {file_name}")
    print("=" * 80)

    for sheet in excel_file.sheet_names:

        print(f"\nSheet: {sheet}")

        df = pd.read_excel(
            file_path,
            sheet_name=sheet,
            header=0
        )

        df = normalize_company_id(df)

        validate_dataset(df)