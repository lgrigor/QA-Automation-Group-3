from collections import namedtuple
import collections
from typing import Counter

class_employee=namedtuple('employee',['emp_id', 'emp_name','job_name','manager_id','salary', 'dep_id'])
employee1=class_employee(10024, 'Hadley_Sylvan', 'QA_Engineer',  9523,  1250, 4)
employee2=class_employee(10037, 'Marcie_Elodie', 'RnD_Engineer', 9012,  1500, 4)
employee3=class_employee(10164, 'Eileen_Candi',  'RnD_Engineer', 9012,  1500, 4) 
employee4=class_employee(10021, 'Floretta_Ike',  'QA_Engineer',  9523,  750,  4)
employee5=class_employee(10094, 'Gideon_Talia',  'QA_Engineer',  9567,  500,  5)

x=0

for employee in (employee1, employee2, employee3, employee4, employee5):
    x+=employee[4]
    print(x)



for employee in (employee1, employee2, employee3, employee4, employee5):
    if employee[4]>=1250:
        print (employee[1])


for employee in (employee1, employee2, employee3, employee4, employee5):
    if employee[5]==4:
        print(employee[1], employee[2])


for employee in (employee1, employee2, employee3, employee4, employee5):
    if employee[3]==9523:
        print(employee[1], employee[0])



for employee in (employee1, employee2, employee3, employee4, employee5):
    if employee[2]==("QA_Engineer"):
     print (employee[0::])








