WITH CommissionData AS (
    SELECT
        sales.saleid,
        sales.saledate,
        agencies.agencyid,
        agencies.agencyname,
        agencies.ownerfirstname,
        agencies.ownerlastname,
        CASE
            WHEN contractname = 'Basic' THEN 0.05 * contractgrossvalue
            WHEN contractname = 'Extended' THEN 0.06 * contractgrossvalue
            WHEN contractname = 'Business' THEN 0.07 * contractgrossvalue
        ELSE 0
        END AS sales_representative_commission
        FROM sales
        JOIN salesrepresentatives
        ON sales.salesrepresentativeid = salesrepresentatives.salesrepresentativeid        
        JOIN agencies
        ON sales.agencyid = agencies.agencyid
)
    SELECT
        agencyid,
        agencyname,
        ownerfirstname,
        ownerlastname,
        EXTRACT (YEAR FROM saledate) AS year,
        EXTRACT (MONTH FROM saledate) AS month,
        SUM(sales_representative_commission)
    FROM CommissionData
    GROUP BY agencyid, agencyname, ownerfirstname, ownerlastname, EXTRACT(YEAR FROM saledate), EXTRACT(MONTH FROM saledate)
    ORDER BY year, month, agencyid;