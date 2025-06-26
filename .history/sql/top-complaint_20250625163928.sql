/* Most common complaints across NYC */

SELECT complaint_type, count (*) as total_complaints
FROM complaints
GROUP BY complaint_type
ORDER BY total_complaints DESC;



SELECT * FROM complaints
where complaint_type = 'Tattooing'
/*
One unique complaint type, 'Tattooing', caught my attention.
I looked into it and found it was a complaint against a tattoo parlor
for using unhygienic and inadequate equipment.
*/
