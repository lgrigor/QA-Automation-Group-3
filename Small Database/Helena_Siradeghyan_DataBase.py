'''Create Employee data type with attributes emp_id, emp_name, job_name, manager_id, salary, dep_id
Integer - emp_id, manager_id, salary, dep_id
String - emp_name, job_name
Tasks:
1. Print the total amount of the salary.
2. Print the names of all employees whose salary is greater than or equal to 1250.
3. Print the names and job names of all employees whose department ID is 4.
4. Print the names then IDs of all employees whose manager ID is 9523.
5. Print the IDs, names and salaries of all QA engineers.
'''

from collections import namedtuple

class_employee = namedtuple("employee",["emp_id","emp_name","job_name","manager_id","salary","dep_id"])
employee_1 = class_employee(10024,"Hadley_Sylvan","QA_Engineer",9523,1250,4)
employee_2 = class_employee(10037,"Marcie_Elodie","RnD_Engineer",9012,1500,4)
employee_3 = class_employee(10164,"Eileen_Candi","RnD_Engineer",9012,1500,4)
employee_4 = class_employee(10021,"Floretta_Ike","QA_Engineer",9523,750,4)
employee_5 =  class_employee(10094,"Gideon_Talia","QA_Engineer",9567,500,5)

employeesalary = 0
employeeinfo = list()
employeedepartmentid = list()
employeemanager_id = list()
employeeQAEngineers = list()

for employee in (employee_1,employee_2,employee_3, employee_4,employee_5):
    employeesalary+=employee.salary
    if employee.salary>=1250:
        employeeinfo.append(employee.emp_name)
    if employee.dep_id == 4:
        employeedepartmentid.append(employee.emp_name+":"+ employee.job_name)
    if employee.manager_id == 9523:
        employeemanager_id.append(str(employee.emp_id) + " : " + employee.emp_name)
    if employee.job_name == "QA_Engineer":
        employeeQAEngineers.append(str(employee.emp_id) + ' ' + employee.emp_name + ' ' +    str(employee.salary))

print(" total amount of the salary",employeesalary,)
print("whose salary is greater than or equal to 1250")
print(employeeinfo)
print("names and job names of all employees whose department ID is 4.")
print(employeedepartmentid)
print('names then IDs of all employees whose manager ID is 9523.')
print(employeemanager_id)
print('the IDs, names and salaries of all QA engineers.')
print(employeeQAEngineers)
