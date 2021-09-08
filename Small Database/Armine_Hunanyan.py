from collections import namedtuple

Employee = namedtuple("Employee", ["emp_id", "emp_name", "job_name", "manager_id", "salary", "dep_id"])

Employee_1 = Employee(10024, "Hadley_Sylvan", "QA_Engineer", 9523, 1250, 4)
Employee_2 = Employee(10037, "Marcie_Elodie", "RnD_Engineer", 9012, 1500, 4)
Employee_3 = Employee(10164, "Eileen_Candi", "RnD_Engineer", 9012, 1500, 4)
Employee_4 = Employee(10021, "Floretta_Ike", "QA_Engineer", 9523, 750, 4)
Employee_5 = Employee(10094, "Gideon_Talia", "QA_Engineer", 9567, 500, 5)

total_salary = 0
for employee in (Employee_1, Employee_2, Employee_3, Employee_4, Employee_5):
    salary = employee.salary
    total_salary += salary
print(total_salary)


for employee in (Employee_1, Employee_2, Employee_3, Employee_4, Employee_5):
     if employee.salary >= 1250:
         print(employee.emp_name)


for employee in (Employee_1, Employee_2, Employee_3, Employee_4, Employee_5):
	if employee.dep_id == 4:
		print(employee.emp_name, employee.job_name)


for employee in (Employee_1, Employee_2, Employee_3, Employee_4, Employee_5):
	if employee.manager_id == 9523:
		print (employee.emp_name)
		print(employee.emp_id)


for employee in (Employee_1, Employee_2, Employee_3, Employee_4, Employee_5):
	if employee.job_name == 'QA_Engineer':
		print (employee.emp_name,employee.emp_id,employee.salary)
