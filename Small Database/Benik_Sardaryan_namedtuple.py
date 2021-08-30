from collections import namedtuple


emp = namedtuple("Employee", ["emp_id", "emp_name", "job_name", "manager_id", "salary", "dep_id"])

emp1 = emp(10024, "Hadley_Sylvan", "QA_Engineer", 9523, 1250, 4)
emp2 = emp(10037, "Marcie_Elodie", "RnD_Engineer", 9012, 1500, 4)
emp3 = emp(10164, "Eileen_Candi", "RnD_Engineer", 9012, 1500, 4)
emp4 = emp(10021, "Floretta_Ike", "QA_Engineer", 9523, 750, 4)
emp5 = emp(10094, "Gideon_Talia", "QA_Engineer", 9567, 500, 5)
emp_all = (emp1, emp2, emp3, emp4, emp5)


# Print the total amount of the salary.

print("Общая зарплата:", sum(emp.salary for emp in emp_all))


# Новая строка

print()


# Print the names of all employees whose salary is greater than or equal to 1250.

for emp in (emp_all):
    if emp.salary >= 1250:
        print("Зарплата выше 1250:", emp.emp_name)


# Новая строка

print()


# Print the names and job names of all employees whose department ID is 4.

for emp in (emp_all):
    if emp.dep_id == 4:
        print("Сотрудники с 4-ого департамента:", emp.emp_name + ",", "Должность:", emp.job_name)


# Новая строка

print()


# Print the names then IDs of all employees whose manager ID is 9523.

for emp in (emp_all):
    if emp.manager_id == 9523:
        print("Сотрудники менеджера ID 9523:", emp.emp_name + ",", "ID сотрудника:", emp.emp_id)


# Новая строка

print()


# Print the IDs, names and salaries of all QA engineers.

for emp in (emp_all):
    if emp.job_name == "QA_Engineer":
        print("QA инженеры: ID -", str(emp.emp_id) + ", Имя -", emp.emp_name + ", Зарплата -", emp.salary)