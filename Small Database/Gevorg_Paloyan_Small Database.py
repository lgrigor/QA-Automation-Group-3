from collections import namedtuple, ChainMap

Employee = namedtuple('Employee', ['emp_id', 'emp_name', 'job_name', 'manager_id', 'salary', 'dep_id'])

empl1 = Employee(10024, 'Jeckie_Chan', 'QA_Engineer', 9523, 1250, 4)
empl2 = Employee(100237, 'Elon_Masc', 'RnD_Engineer', 9012, 1500, 4)
empl3 = Employee(10164, 'Djan_Klode', 'RnD_Engineer', 1500, 1250, 4)
empl4 = Employee(10021, 'Ringi_Kuture', 'QA_Engineer', 9523, 750, 4)
empl5 = Employee(10094, 'Muhamed_Alii', 'QA_Engineer', 9567, 500, 5)

employeeSalary = 0
emplNameList = list()
emplDepIDis4 = list()
emplManagerID = list()
empQAEngineers = list()

for employee in (empl1, empl2, empl3, empl4, empl5):
   employeeSalary += employee.salary
   if employee.salary >= 1250:
       emplNameList.append(employee.emp_name)
   if employee.dep_id == 4:
       emplDepIDis4.append(employee.emp_name + " : " + employee.job_name)
   if employee.manager_id == 9523:
       emplManagerID.append(employee.emp_name + " : " + str(employee.emp_id))
   if employee.job_name == 'QA_Engineer':
       empQAEngineers.append(str(employee.emp_id) + ' ' + employee.emp_name + ' ' +        str(employee.salary))

print('1. total amount of the salary', employeeSalary, '\n')

print("2. employees whose salary is greater than or equal to 1250")
print(emplNameList, '\n')

print("3. names and job names of all employees whose department ID is 4.")
print(emplDepIDis4, '\n')

print('4.  names then IDs of all employees whose manager ID is 9523.')
print(emplManagerID, '\n')

print('5.  the IDs, names and salaries of all QA engineers.')
print(empQAEngineers)

