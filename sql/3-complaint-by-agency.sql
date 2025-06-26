Select agency_name, Count (*) AS total_complaints
from complaints
GROUP BY agency_name
ORDER BY total_complaints DESC;





