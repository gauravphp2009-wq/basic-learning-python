-- SQL analysis queries for the PythonSparks eCommerce pipeline

-- 1) Total revenue and units sold by product category
SELECT category,
       SUM(sales_amount) AS total_revenue,
       SUM(quantity) AS total_units,
       SUM(gross_margin) AS total_margin
FROM fact_orders
GROUP BY category
ORDER BY total_revenue DESC;

-- 2) Top 10 customers by revenue
SELECT full_name,
       email,
       SUM(sales_amount) AS customer_revenue,
       COUNT(DISTINCT order_id) AS order_count
FROM fact_orders
GROUP BY full_name, email
ORDER BY customer_revenue DESC
LIMIT 10;

-- 3) Monthly revenue trend
SELECT date_format(order_date, 'yyyy-MM') AS month,
       SUM(sales_amount) AS revenue
FROM fact_orders
GROUP BY date_format(order_date, 'yyyy-MM')
ORDER BY month;

-- 4) Orders with missing dimension data for debugging
SELECT *
FROM fact_orders
WHERE validation_status = 'MISSING_DIMENSION';
