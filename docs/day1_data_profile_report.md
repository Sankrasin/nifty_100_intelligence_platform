Day 1 Data Profile Report

Project

Nifty 100 Financial Intelligence Platform

Objective

Validate all provided datasets and understand their structure before beginning ETL and analytics development.

Activities Completed

1. Environment Setup

* Created project folder structure.
* Created Python virtual environment: venv_nifty.
* Installed required libraries from requirements.txt.

2. Dataset Loading

Successfully loaded all 12 datasets:

Dataset	Records
companies.xlsx	92
profitandloss.xlsx	1,276
balancesheet.xlsx	1,312
cashflow.xlsx	1,187
analysis.xlsx	20
documents.xlsx	1,585
prosandcons.xlsx	16
sectors.xlsx	92
stock_prices.xlsx	5,520
market_cap.xlsx	552
financial_ratios.xlsx	1,184
peer_groups.xlsx	56

3. Data Validation

Performed:

* Shape checks
* Data type inspection
* Missing value analysis
* Duplicate row checks
* Sample record verification
* Primary key validation

Key Findings

* Core datasets require header=1.
* Supplementary datasets require header=0.
* Company identifiers are NSE tickers.
* Several datasets contain missing values that will be handled during data cleaning.
* No major loading issues found.
* All datasets successfully imported into Pandas.

Deliverables Created

* src/etl/load_excel.py
* src/etl/validate_data.py

Status

Sprint 1 – Day 1 completed successfully.

Next Step:
Sprint 1 – Day 2: Data Cleaning & Standardization.