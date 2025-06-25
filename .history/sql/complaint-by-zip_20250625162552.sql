SELECT incident_zip, 
city,
count(*) as total_complaints
from complaints
GROUP BY city, incident_zip 
ORDER BY total_complaints DESC
Limit 20



/*MAX NO. OF COMLAINTS WERE FROM BROOKLYN. SO CHECKED THE COUNT*/
SELECT count(*) AS total_brooklyn_complaints
FROM complaints
WHERE city = 'BROOKLYN';