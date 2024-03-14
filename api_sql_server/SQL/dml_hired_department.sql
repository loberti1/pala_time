with initial as(
SELECT ISNULL(h.id_departments, 0) as 'id', ISNULL(d.ds_departments,'N/A') as 'departments', YEAR(h.id_datetime) as 'Year'
,COUNT(h.id_custom_hired_employee) as 'hired'
FROM hired_employees h left join departments d ON h.id_departments = d.id_departments
					   left join jobs j on h.id_jobs = j.id_jobs
WHERE YEAR(h.id_datetime) = '2021'
GROUP BY ISNULL(h.id_departments, 0), ISNULL(d.ds_departments,'N/A'),  YEAR(h.id_datetime)
HAVING COUNT(h.id_custom_hired_employee) > (SELECT COUNT(h.id_custom_hired_employee)/COUNT(DISTINCT(ISNULL(h.id_departments,0)))
											FROM hired_employees h left join departments d ON h.id_departments = d.id_departments
																	left join jobs j on h.id_jobs = j.id_jobs
											WHERE YEAR(h.id_datetime) = '2021'))
SELECT id, departments, hired FROM initial
order by hired DESC