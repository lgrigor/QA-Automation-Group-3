from collections import namedtuple

def task_1():
    print(sum([each_employee.salary for each_employee in all]))

def task_2():
    for each_employee in all:
        if each_employee.salary >= 1250:
            print(each_employee.emp_name)

def task_3():
    for each_employee in all:
        if each_employee.dep_id == 4:
            print(each_employee.emp_name, each_employee.job_name)

def task_4():
    for each_employee in all:
        if each_employee.manager_id == 9523:
            print(each_employee.emp_name, each_employee.emp_id)

def task_5():
    for each_employee in all:
        if each_employee.job_name == 'QA_Engineer':
            print(each_employee.emp_id, each_employee.emp_name)


employee = namedtuple('employee', ['emp_id', 'emp_name', 'job_name', 'manager_id', 'salary', 'dep_id'])

employee_1 = employee(10024, 'Hadley_Sylvan', 'QA_Engineer', 9523, 1250, 4)
employee_2 = employee(10037, 'Marcie_Elodie', 'RnD_Engineer', 9012, 1500, 4)
employee_3 = employee(10164, 'Eileen_Candi', 'RnD_Engineer', 9012, 1500, 4)
employee_4 = employee(10021, 'Floretta_Ike', 'QA_Engineer', 9523, 750, 4)
employee_5 = employee(10094, 'Gideon_Talia', 'QA_Engineer', 9567, 500, 5)

all = (employee_1, employee_2, employee_3, employee_4, employee_5)

print('1. Print the total amount of the salary.')
task_1()

print('\n2. Print the names of all employees whose salary is greater than or equal to 1250.')
task_2()

print('\n3. Print the names and job names of all employees whose department ID is 4.')
task_3()

print('\n4. Print the names then IDs of all employees whose manager ID is 9523.')
task_4()

print('\n5. Print the IDs, names and salaries of all QA engineers.')
task_5()
