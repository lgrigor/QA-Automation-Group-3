from collections import namedtuple

Employee = namedtuple('Employee', ['emp_id', 'emp_name', 'job_name', 'manager_id', 'salary', 'dep_id'])

employee1 = Employee(101, 'Jan', 'QA_Engineer', 9500, 1000, 4)
employee2 = Employee(102, 'Pol', 'developer', 9521, 1200, 4)
employee3 = Employee(103, 'Messi', 'manager', 9522, 1500, 4)
employee4 = Employee(104, 'Kan', 'QA_Engineer1', 9523, 1100, 4)
employee5 = Employee(105, 'Van', 'QA_Engineer2', 9524, 1300, 5)

emplsalary = 0
emplid = list()
empldep = list()
emplmanager = list()
empljob = list()

for employee in (employee1, employee2, employee3, employee4, employee5):
   emplsalary += employee.salary
   if employee.salary >= 1250:
       emplid.append(employee.emp_name)
   if employee.dep_id == 4:
       empldep.append(employee.emp_name + " : " + employee.job_name)
   if employee.manager_id == 9523:
       emplmanager.append(employee.emp_name + " : " + str(employee.emp_id))
   if employee.job_name == 'QA_Engineer':
       empljob.append(str(employee.emp_id) + ' ' + employee.emp_name + ' ' +        str(employee.salary))

print('the total amount of the salary')
print(emplsalary)

print("the names of all employees whose salary is greater than or equal to 1250")
print(emplid)

print("the names and job names of all employees whose department ID is 4")
print(empldep)

print('the names then IDs of all employees whose manager ID is 9523')
print(emplmanager)

print('the IDs, names and salaries of all QA engineers')
print(empljob)