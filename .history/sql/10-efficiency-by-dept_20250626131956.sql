SELECT 
    agency_name, 
    COUNT(*) AS total_complaints,
    SUM(CASE WHEN closed_date IS NOT NULL THEN 1 ELSE 0 END) AS total_close_cases
FROM complaints
GROUP BY agency_name
ORDER BY total_complaints DESC, total_close_cases DESC;