from collections import namedtuple

# Create Employee data type with attributes emp_id, emp_name, job_name, manager_id, salary, dep_id
# Integer - emp_id, manager_id, salary, dep_id
# String - emp_name, job_name
#
# Create 5 employee objects. Attributes of each employee are attached.
#
# Tasks:
# 1. Print the total amount of the salary.
# 2. Print the names of all employees whose salary is greater than or equal to 1250.
# 3. Print the names and job names of all employees whose department ID is 4.
# 4. Print the names then IDs of all employees whose manager ID is 9523.
# 5. Print the IDs, names and salaries of all QA engineers.

def salary_total_amount(*args):
        print("Total amount of the salary: ")
        print(sum(x.salary for x in args))

def greater_salary(*args):
    for x in args:
        if x.salary >= 1250:
            print("Names of employees whose salary is greater than or equal to 1250: ",  x.emp_name)        
        
Employee = namedtuple('Employee',['emp_id','emp_name','job_name','manager_id','salary','dep_id'])

employee1 = Employee(10024, 'Hadley_Sylvan', 'QA_Engineer', 9523, 1250, 4)

employee2 = Employee(10037, 'Marcie_Elodie', 'RnD_Engineer', 9012, 1500, 4)

employee3 = Employee(10164, 'Eileen_Candi', 'RnD_Engineer', 9012, 1500, 4)

employee4 = Employee(10021, 'Floretta_Ike', 'QA_Engineer', 9523, 750, 4)

employee5 = Employee(10094, 'Gideon_Talia', 'QA_Engineer', 9567, 500, 5)


# Tasks:
# 1. Print the total amount of the salary.



salary_total_amount(employee5, employee4, employee3, employee2, employee1)



# 2. Print the names of all employees whose salary is greater than or equal to 1250.




greater_salary(employee5, employee4, employee3, employee2, employee1)


# 3. Print the names and job names of all employees whose department ID is 4.


def dep_id(*args):
    for x in args:
        if x.dep_id == 4:
            print("Names and job names of all employees whose department ID is 4 : ", x.emp_name, "-" , x.job_name)
        # print(x.salary)
        # print("The total amount of the salary")


dep_id(employee5, employee4, employee3, employee2, employee1)


# 4. Print the names then IDs of all employees whose manager ID is 9523.


def manager_id(*args):
    for x in args:
        if x.manager_id == 9523:
            print("Names:", x.emp_name, ";", "IDS:", x.emp_id)
        # print(x.salary)
        # print("The total amount of the salary")


manager_id(employee5, employee4, employee3, employee2, employee1)


# 5. Print the IDs, names and salaries of all QA engineers.

def qa_engineers(*args):
    for x in args:
        if x.job_name == 'QA_Engineer':
            print("Job:", x.job_name, "_", "IDs:", x.emp_id, ";",  " Names:", x.emp_name, ";", " Salaries:", x.salary)
        # print(x.salary)
        # print("The total amount of the salary")


qa_engineers(employee5, employee4, employee3, employee2, employee1)
