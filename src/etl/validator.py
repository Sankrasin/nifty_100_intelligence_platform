import pandas as pd
from pathlib import Path

from src.etl.loader import load_core_excel

PROJECT_ROOT = Path(__file__).resolve().parents[2]

REPORTS_DIR = PROJECT_ROOT / "reports"

REPORTS_DIR.mkdir(
    exist_ok=True
)

failures = []


def log_failure(
    dataset,
    rule,
    company_id,
    year,
    issue
):

    failures.append(
        {
            "dataset": dataset,
            "rule": rule,
            "company_id": company_id,
            "year": year,
            "issue": issue
        }
    )


companies = load_core_excel(
    "companies.xlsx"
)

valid_companies = set(
    companies["id"]
)

# ==================================================
# PROFIT AND LOSS
# ==================================================

pl = load_core_excel(
    "profitandloss.xlsx"
)

for _, row in pl.iterrows():

    if pd.isna(row["company_id"]):

        log_failure(
            "profitandloss",
            "DQ001",
            None,
            row.get("year"),
            "company_id missing"
        )

    elif row["company_id"] not in valid_companies:

        log_failure(
            "profitandloss",
            "DQ002",
            row["company_id"],
            row["year"],
            "company not found in companies"
        )

    if pd.isna(row["year"]):

        log_failure(
            "profitandloss",
            "DQ003",
            row["company_id"],
            None,
            "year missing"
        )

    if row["sales"] <= 0:

        log_failure(
            "profitandloss",
            "DQ005",
            row["company_id"],
            row["year"],
            "sales <= 0"
        )

dup = pl.duplicated(
    subset=["company_id", "year"],
    keep=False
)

for _, row in pl[dup].iterrows():

    log_failure(
        "profitandloss",
        "DQ004",
        row["company_id"],
        row["year"],
        "duplicate company-year"
    )

# ==================================================
# BALANCE SHEET
# ==================================================

bs = load_core_excel(
    "balancesheet.xlsx"
)

for _, row in bs.iterrows():

    diff = abs(
        row["total_assets"]
        -
        row["total_liabilities"]
    )

    if diff > 1:

        log_failure(
            "balancesheet",
            "DQ006",
            row["company_id"],
            row["year"],
            f"assets-liabilities diff={diff}"
        )

# ==================================================
# OPERATING PROFIT CHECK
# ==================================================

for _, row in pl.iterrows():

    if pd.isna(
        row["operating_profit"]
    ):
        continue

    expected = (
    row["sales"]
    - row["expenses"]
    )

    if row["sales"] == 0:
        continue

    diff_pct = (
        abs(
            row["operating_profit"]
            - expected
        )
        / row["sales"]
        * 100
    )

    if diff_pct > 1:

        log_failure(
            "profitandloss",
            "DQ007",
            row["company_id"],
            row["year"],
            "operating profit mismatch"
        )

# ==================================================
# CASH FLOW
# ==================================================

cf = load_core_excel(
    "cashflow.xlsx"
)

for _, row in cf.iterrows():

    if pd.isna(
        row["net_cash_flow"]
    ):
        continue

    expected = (
        row["operating_activity"]
        +
        row["investing_activity"]
        +
        row["financing_activity"]
    )

    diff = abs(
        row["net_cash_flow"]
        -
        expected
    )

    if diff > 10:

        log_failure(
            "cashflow",
            "DQ008",
            row["company_id"],
            row["year"],
            "cashflow mismatch"
        )

# ==================================================
# SAVE REPORT
# ==================================================

failure_df = pd.DataFrame(
    failures
)

output_file = (
    REPORTS_DIR
    /
    "validation_failures.csv"
)

failure_df.to_csv(
    output_file,
    index=False
)

print("\nValidation Complete")
print(
    f"Failures Found: {len(failure_df)}"
)
print(
    f"Saved: {output_file}"
)