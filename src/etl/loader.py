import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_DATA = PROJECT_ROOT / "data" / "raw"
SUPPORTING_DATA = PROJECT_ROOT / "data" / "supporting"

CORE_FILES = [
    "companies.xlsx",
    "profitandloss.xlsx",
    "balancesheet.xlsx",
    "cashflow.xlsx",
    "analysis.xlsx",
    "documents.xlsx",
    "prosandcons.xlsx"
]

SUPPORTING_FILES = [
    "financial_ratios.xlsx",
    "market_cap.xlsx",
    "peer_groups.xlsx",
    "sectors.xlsx",
    "stock_prices.xlsx"
]


def normalize_ticker(ticker):
    if pd.isna(ticker):
        return None

    return str(ticker).strip().upper()


def normalize_year(year):

    if pd.isna(year):
        return None

    year = str(year).strip()

    try:

        if "-" in year:

            parts = year.split("-")

            if len(parts) == 2:

                month = parts[0]
                yy = parts[1]

                if yy.isdigit() and len(yy) == 2:

                    full_year = 2000 + int(yy)

                    dt = pd.to_datetime(
                        f"{month}-{full_year}",
                        format="%b-%Y"
                    )

                    return dt.strftime("%Y-%m")

        dt = pd.to_datetime(year)

        return dt.strftime("%Y-%m")

    except Exception:

        return year


def load_core_excel(file_name):
    file_path = RAW_DATA / file_name

    df = pd.read_excel(
        file_path,
        header=1
    )
    if "id" in df.columns:
        df["id"] = df["id"].apply(
            normalize_ticker
        )

    if "company_id" in df.columns:
        df["company_id"] = (
            df["company_id"]
            .apply(normalize_ticker)
        )

    if "year" in df.columns:
        df["year"] = (
            df["year"]
            .apply(normalize_year)
        )

    return df


def load_supporting_excel(file_name):
    file_path = SUPPORTING_DATA / file_name

    df = pd.read_excel(
        file_path,
        header=0
    )

    if "company_id" in df.columns:
        df["company_id"] = (
            df["company_id"]
            .apply(normalize_ticker)
        )

    if "year" in df.columns:
        df["year"] = (
            df["year"]
            .apply(normalize_year)
        )

    return df


def load_all_core():
    datasets = {}

    for file in CORE_FILES:
        datasets[file] = load_core_excel(file)

    return datasets


def load_all_supporting():
    datasets = {}

    for file in SUPPORTING_FILES:
        datasets[file] = load_supporting_excel(file)

    return datasets


if __name__ == "__main__":

    print("\nCORE DATASETS\n")

    core_data = load_all_core()

    for name, df in core_data.items():
        print(
            f"{name:<25}"
            f"Rows: {df.shape[0]:<6}"
            f"Cols: {df.shape[1]}"
        )