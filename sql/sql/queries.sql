-- 1. Top 5 funds by AUM

SELECT 
    scheme_name,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;


-- 2. Average NAV

SELECT
    AVG(nav) AS average_nav
FROM fact_nav;


-- 3. Total transactions by state

SELECT
    state,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;


-- 4. Funds with expense ratio less than 1%

SELECT
    scheme_name,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;


-- 5. Transaction type count

SELECT
    transaction_type,
    COUNT(*) AS count
FROM fact_transactions
GROUP BY transaction_type;
-- 6. Monthly average NAV trend

SELECT
    strftime('%Y-%m', date) AS month,
    AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;


-- 7. SIP vs Lumpsum vs Redemption count

SELECT
    transaction_type,
    COUNT(*) AS total
FROM fact_transactions
GROUP BY transaction_type;


-- 8. Top 5 cities by transactions

SELECT
    city,
    COUNT(*) AS transactions
FROM fact_transactions
GROUP BY city
ORDER BY transactions DESC
LIMIT 5;


-- 9. High risk funds with returns

SELECT
    scheme_name,
    risk_grade,
    return_3yr_pct
FROM fact_performance
WHERE risk_grade = 'Very High'
ORDER BY return_3yr_pct DESC;


-- 10. Average return by category

SELECT
    category,
    AVG(return_3yr_pct) AS avg_return
FROM fact_performance
GROUP BY category;