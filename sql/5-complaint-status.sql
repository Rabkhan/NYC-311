Select count (*) as total_complaints, status
FROM complaints
Group BY status
ORDER BY total_complaints DESC;