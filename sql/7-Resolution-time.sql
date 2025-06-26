SELECT
  complaint_type,
   ROUND(AVG(closed_date::date - created_date::date)) AS avg_resolution_time_days
FROM complaints
WHERE closed_date IS NOT NULL AND created_date IS NOT NULL
GROUP BY complaint_type
ORDER BY avg_resolution_time_days DESC;

/* 0 Days mean - Resolved on the same dat*/