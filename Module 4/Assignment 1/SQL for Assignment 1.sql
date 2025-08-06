create database assignment1;
use assignment1;

create table google_salaries (
id INT primary key, 
first_name varchar(100),
last_name varchar(100),
department varchar(100),
education varchar(100),
salary int
);

select * from google_salaries;

-- Task 1
select * from google_salaries
where salary >5000; 

-- Task 2 google_salaries

Select first_name, department, education
from google_salaries
where first_name like "Ma%";

-- Task 3
select distinct department
from google_salaries;


-- Task 4
select education, sum(salary) as Total_salary
from google_salaries
group by education;