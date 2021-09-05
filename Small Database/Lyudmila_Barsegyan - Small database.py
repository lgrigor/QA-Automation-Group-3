from collections import namedtuple

Employee = namedtuple("Employee", ["emp_id", "emp_name", "job_name", "manager_id", "salary", "dep_id"])

Employee_1 = Employee(10024, "Hadley_Sylvan", "QA_Engineer", 9523, 1250, 4)
Employee_2 = Employee(10037, "Marcie_Elodie", "RnD_Engineer", 9012, 1500, 4)
Employee_3 = Employee(10164, "Eileen_Candi", "RnD_Engineer", 9012, 1500, 4)
Employee_4 = Employee(10021, "Floretta_Ike", "QA_Engineer", 9523, 750, 4)
Employee_5 = Employee(10094, "Gideon_Talia", "QA_Engineer", 9567, 500, 5)

salary_sum = 0
for employee in (Employee_1, Employee_2, Employee_3, Employee_4, Employee_5):
    salary = employee.salary
    salary_sum += salary

print("The total amount of the salary is: {}".format(salary_sum))


for employee in (Employee_1, Employee_2, Employee_3, Employee_4, Employee_5):
     if employee.salary >= 1250:
         print("The names of all employees whose salary is greater than or equal to 1250: {}".format(employee.emp_name))

    
for employee in (Employee_1, Employee_2, Employee_3, Employee_4, Employee_5):
    if employee.dep_id == 4:
        print("The names and job names of all employees whose department ID is 4: {} {}".format(employee.emp_name, employee.job_name)) 


for employee in (Employee_1, Employee_2, Employee_3, Employee_4, Employee_5):
    if employee.manager_id == 9523:
         print("The names then IDs of all employees whose manager ID is 9523: {} {}".format(employee.emp_name, employee.emp_id)) 


for employee in (Employee_1, Employee_2, Employee_3, Employee_4, Employee_5):
     if employee.job_name == "QA_Engineer":
          print("The IDs, names and salaries of all QA engineers: {} {} {}".format(employee.emp_id, employee.emp_name, employee.salary)) 