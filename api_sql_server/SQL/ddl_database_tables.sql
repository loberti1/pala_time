create database glob_dw;
create table departments 
(
id_departments INT PRIMARY KEY NOT NULL,
ds_departments VARCHAR(100)
);

create table jobs 
(
id_jobs INT PRIMARY KEY NOT NULL,
ds_jobs VARCHAR(100)
);

create table hired_employees 
(
id_custom_hired_employee INT PRIMARY KEY NOT NULL,
ds_hired_employee VARCHAR(100),
id_datetime DATETIME,
id_departments INT,
id_jobs INT
);