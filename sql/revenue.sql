DROP TABLE IF EXISTS revenue;

CREATE TABLE revenue AS
WITH RECURSIVE calendar(date_id) AS (
    SELECT DATE('2025-01-01')
    UNION ALL
    SELECT DATE(date_id, '+1 day')
    FROM calendar
    WHERE date_id < '2025-01-31'
)

SELECT
    p.sku_id,
    c.date_id,
    p.price,
    COALESCE(SUM(s.sales), 0) AS sales,
    p.price * COALESCE(SUM(s.sales), 0) AS revenue

FROM product p
CROSS JOIN calendar c
LEFT JOIN sales s
    ON p.sku_id = s.sku_id
    AND DATE(s.orderdate_utc) = c.date_id
GROUP BY
    p.sku_id,
    c.date_id,
    p.price
ORDER BY
    p.sku_id,
    c.date_id;