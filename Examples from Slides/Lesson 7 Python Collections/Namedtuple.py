from collections import namedtuple

class_employee = namedtuple('employee', ['name', 'exp'], defaults=['Ivan', '0'])

employee_1 = class_employee('Wandersar', 5)
employee_2 = class_employee('Boerland', 3)
employee_3 = class_employee('Vladislav')

my_list = ['Nandini', '10']
employee_4 = class_employee._make(my_list)

my_dict = employee_4._asdict()
#print(my_dict['name'])

my_dict = {'name': 'Olive', 'exp': 1}
employee_5 = class_employee(**my_dict)
#print(employee_5)

#print(employee_5._fields)
employee_5 = class_employee._replace(employee_5, exp=2)
print(employee_5)
exit(1)

#for employee in (employee_1, employee_2, employee_3, employee_4):
#    print(employee.exp)



