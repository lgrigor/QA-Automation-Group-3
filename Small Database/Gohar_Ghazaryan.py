from collections import namedtuple

def total_salary (employees):
    total_salary = 0
    for empl in employees:
        total_salary = total_salary + (getattr(empl,'salary'))
    return total_salary

def rich_employees (employees):
    min_salary = 1250
    for empl in employees:
        current_salary = (getattr(empl,'salary'))
        if current_salary >= min_salary :
            print(getattr(empl,'emp_name'), " : ", getattr(empl,'salary'))

def from_dep_employess (employees, dpm_id = 4):
    print(" Employees from", dpm_id, "-th department : ")
    for empl in employees:
        department_id = (getattr(empl,'dep_id'))    
        if department_id == dpm_id:
            print(getattr(empl,'emp_name'), " -> ", getattr(empl, 'job_name'))

def manager_employess (employees, m_id = 9523):
    print(m_id, " Manager's team ")
    for empl in employees:
        manager_id = (getattr(empl,'manager_id'))    
        if manager_id == m_id:
            print(getattr(empl,'emp_name'), " -> ", getattr(empl, 'emp_id'))

def info_per_position (employees, position = 'QA_Engineer'):
    print(position, "'s")
    for empl in employees:
        job_name = (getattr(empl,'job_name'))    
        if job_name == position:
            print(getattr(empl, 'emp_id'), getattr(empl,'emp_name'), " -> ", getattr(empl, 'salary'))

Employee = namedtuple ('Employee', ['emp_id', 'emp_name', 'job_name', 'manager_id', 'salary', 'dep_id'])

employee_1 = Employee (10024, 'Hadley_Sylvan', 'QA_Engineer', 9523, 1250, 4)
employee_2 = Employee (10037, 'Marcie_Elodie', 'RnD_Engineer', 9012, 1500, 4)
employee_3 = Employee (10164, 'Eileen_Candi', 'RnD_Engineer', 9012, 1500, 4)
employee_4 = Employee (10021, 'Floretta_Ike', 'QA_Engineer', 9523, 750, 4)
employee_5 = Employee (10094, 'Gideon_Talia', 'QA_Engineer',9567, 500, 5)


employee_list = [employee_1, employee_2, employee_3, employee_4, employee_5]
#print ("The total amount of salary using getattr() is : ",end ="")
#print(total_salary(employee_list))

print ("The rich employees are : ")
rich_employees(employee_list)

from_dep_employess(employee_list, 4)
manager_employess(employee_list)
info_per_position(employee_list)







