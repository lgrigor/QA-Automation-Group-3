# Exercise 1: Below are the two lists convert it into the dictionary

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
new_dict = dict(zip(keys, values))
print(new_dict)

# Exercise 2: Create a new dictionary with the following keys from a below dictionary

sample_dict = {
 "name": "Kelly",
 "age":25,
 "salary": 8000,
 "city": "New york" }

keys = ["name", "salary"]
new_dict = {i: sample_dict[i] for i in keys}
print(new_dict)

# Exercise 3: Access the value of key ‘history’ from the below dict

get_dict_value = {
   "class":{
       "student":{
           "name":"Mike",
           "marks":{
               "physics":70,
               "history":80
           }
       }
   }
}
print(get_dict_value['class']['student']['marks']['history'])

# Exercise 4: Change Brad’s salary to 8500 from a given Python dictionary

my_dict = {
   'emp1': {'name': 'Jhon', 'salary': 7500},
   'emp2': {'name': 'Emma', 'salary': 8000},
   'emp3': {'name': 'Brad', 'salary': 6500}
}
salary_change = my_dict['emp3']['salary'] = 8500
print(my_dict)
