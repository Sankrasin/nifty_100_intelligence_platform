-- 1. Total companies
SELECT COUNT(*) AS total_companies
FROM companies;

-- 2. Profit & Loss row count
SELECT COUNT(*) AS pnl_rows
FROM profitandloss;

-- 3. Balance Sheet row count
SELECT COUNT(*) AS balance_sheet_rows
FROM balancesheet;

-- 4. Cash Flow row count
SELECT COUNT(*) AS cashflow_rows
FROM cashflow;

-- 5. Companies per sector
SELECT broad_sector,
       COUNT(*) AS company_count
FROM sectors
GROUP BY broad_sector
ORDER BY company_count DESC;

-- 6. Top 10 companies by ROCE
SELECT id,
       roce_percentage
FROM companies
ORDER BY roce_percentage DESC
LIMIT 10;

-- 7. Companies with highest debt
SELECT company_id,
       borrowings
FROM balancesheet
ORDER BY borrowings DESC
LIMIT 10;

-- 8. Year coverage per company
SELECT company_id,
       COUNT(*) AS years_available
FROM profitandloss
GROUP BY company_id
ORDER BY years_available DESC;

-- 9. Missing annual reports
SELECT company_id,
       COUNT(*) AS missing_reports
FROM documents
WHERE Annual_Report IS NULL
GROUP BY company_id;

-- 10. Average PE Ratio
SELECT AVG(pe_ratio) AS avg_pe_ratio
FROM market_cap;