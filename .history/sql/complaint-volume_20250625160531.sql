SELECT DATE(created_date) as date, /*selecting only date from data&timestamp*/
COUNT(*) AS total_complaints
FROM complaints
GROUP BY Date
ORDER BY total_complaints DESC;