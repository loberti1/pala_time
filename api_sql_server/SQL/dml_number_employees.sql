WITH initial as
(
SELECT
h.id_custom_hired_employee,h.ds_hired_employee, YEAR(h.id_datetime) as 'ds_year', MONTH(h.id_datetime) as 'ds_month' , 
case when MONTH(h.id_datetime) >=1 and MONTH(h.id_datetime) <= 3 then 'Q1'
	 when MONTH(h.id_datetime) >=4 and MONTH(h.id_datetime) <= 6 then 'Q2'
	 when MONTH(h.id_datetime) >=7 and MONTH(h.id_datetime) <= 9 then 'Q3'
	 when MONTH(h.id_datetime) >=10 and MONTH(h.id_datetime) <= 12 then 'Q4' end as 'ds_quarter', 
	 ISNULL(j.ds_jobs,'N/A') as 'ds_jobs', ISNULL(d.ds_departments,'N/A') as 'ds_departments'
FROM hired_employees h
left join jobs j on h.id_jobs = j.id_jobs
left join departments d on h.id_departments=d.id_departments
WHERE YEAR(h.id_datetime) = '2021'
)
SELECT ds_departments, ds_jobs,
	   SUM(case when ds_quarter = 'Q1' then 1 else 0 end) as 'Q1',
	   SUM(case when ds_quarter = 'Q2' then 1 else 0 end) as 'Q2',
	   SUM(case when ds_quarter = 'Q3' then 1 else 0 end) as 'Q3',
	   SUM(case when ds_quarter = 'Q4' then 1 else 0 end) as 'Q4'
FROM initial
GROUP BY ds_departments, ds_jobs
ORDER BY ds_departments, ds_jobs