from collections import namedtuple

Employee = namedtuple('Employee', ['emp_id', 'emp_name', 'job_name', 'manager_id', 'salary', 'dep_id'])

employee_1 = Employee(10024, 'Hadley_Sylvan', 'QA_Engineer', 9523, 1250, 4)
employee_2 = Employee(10037, 'Marcie_Elodie', 'RnD_Engineer', 9012, 1500, 4)
employee_3 = Employee(10164, 'Eileen_Candi', 'RnD_Engineer', 9012, 1500, 4)
employee_4 = Employee(10021, 'Floretta_Ike', 'QA_Engineer', 9523, 750, 4)
employee_5 = Employee(10094, 'Gideon_Talia', 'QA_Engineer', 9567, 500, 5)

employee_list = [employee_1, employee_2, employee_3, employee_4, employee_5]

total_amount = 0
name_list = []
dep_id_list = []
manager_id_list = []
job_name_list = []

# 1. Print the total amount of the salary.
for i in employee_list:
   total_amount += i.salary

# 2. Print the names of all employees whose salary is greater than or equal to 1250.
   if i.salary >= 1250:
       name_list.append(i.emp_name)

# 3. Print the names and job names of all employees whose department ID is 4.
   if i.dep_id == 4:
       dep_id_list.extend([i.emp_name, i.job_name])

# 4. Print the names then IDs of all employees whose manager ID is 9523.
   if i.manager_id == 9523:
       manager_id_list.extend([i.emp_name, i.dep_id])

# 5. Print the IDs, names and salaries of all QA engineers.
   if i.job_name == 'QA_Engineer':
       job_name_list.extend([i.dep_id, i.emp_name, i.salary])


print("Total amount of the salary : ", total_amount)
print("Names of all employees whose salary is greater than or equal to 1250 : ", name_list)
print("Names and job names of all employees whose department ID is 4 : ", dep_id_list)
print("Names then IDs of all employees whose manager ID is 9523 : ", manager_id_list)
print("IDs, names and salaries of all QA engineers : ", job_name_list)


