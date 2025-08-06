select department, avg(salary) as average_salary 
from google_salaries
group by department;