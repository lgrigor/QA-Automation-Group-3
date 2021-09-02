from collections import namedtuple

Employee = namedtuple('Employee', ['emp_id', 'emp_name', 'job_name', 'manager_id', 'salary', 'dep_id'])
E_1 = Employee (10024, 'Hadley_Sylvan', 'QA_Engineer', 9523, 1250, 4)
E_2 = Employee (10037, 'Marcie_Elodie', 'RnD_Engineer', 9012, 1500, 4)
E_3 = Employee (10164, 'Eileen_Candi', 'RnD_Engineer', 9012, 1500, 4)
E_4 = Employee (10021, 'Floretta_Ike', 'QA_Engineer', 9523, 750, 4)
E_5 = Employee (10094, 'Gideon_Talia', 'QA_Engineer', 9567, 500, 5)

total = 0

for Employee in (E_1, E_2, E_3, E_4, E_5):
    total += Employee[4]
print(total)
for Employee in (E_1, E_2, E_3, E_4, E_5):
    if Employee[4] >= 1250:
        print(Employee.emp_name)
for Employee in (E_1, E_2, E_3, E_4, E_5):
    if Employee[5] == 4:
        print(Employee.emp_name, Employee.job_name)
for Employee in (E_1, E_2, E_3, E_4, E_5):
    if Employee[3] == 9523:
        print(Employee.emp_name, Employee.emp_id)
for Employee in (E_1, E_2, E_3, E_4, E_5):
    if Employee[2] == 'QA_Engineer':
        print(Employee.emp_id, Employee.emp_name, Employee.salary)

