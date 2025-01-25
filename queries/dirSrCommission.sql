WITH CommissionData AS (
    SELECT
        sales.saleid,
        sales.saledate,
        directors.directorid,
        directors.directorfirstname,
        directors.directorlastname,
        CASE
            WHEN contractname = 'Basic' THEN 0.02 * (0.05 * contractgrossvalue)
            WHEN contractname = 'Extended' THEN 0.03 * (0.06 * contractgrossvalue)
            WHEN contractname = 'Basic' THEN 0.04 * (0.07 * contractgrossvalue)
            ELSE 0
        END AS director_commission
    FROM sales
    JOIN directors ON sales.directorid = directors.directorid
)
SELECT
    directorid,
    directorfirstname,
    directorlastname,
    EXTRACT(YEAR FROM saledate) AS year,
    EXTRACT(MONTH FROM saledate) AS month,
    SUM(director_commission) AS total_director_commission
FROM CommissionData
GROUP BY directorid, directorfirstname, directorlastname, EXTRACT(YEAR FROM saledate), EXTRACT(MONTH FROM saledate)
ORDER BY year, month, directorid;

