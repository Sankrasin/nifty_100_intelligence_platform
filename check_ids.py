from src.etl.loader import load_core_excel

companies = load_core_excel("companies.xlsx")
profit = load_core_excel("profitandloss.xlsx")

missing = set(profit["company_id"]) - set(companies["id"])

print("Missing IDs:")
print(sorted(missing))