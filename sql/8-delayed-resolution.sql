SELECT *
FROM complaints
WHERE closed_date IS NULL AND created_date < NOW() - INTERVAL '7 days';

