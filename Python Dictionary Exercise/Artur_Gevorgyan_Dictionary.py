#Exercise 1: Below are the two lists convert it into the dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dict = dict(zip(keys, values))
print(dict)


#Exercise 2: Create a new dictionary with the following keys from a below dictionary
dict = { 
  "name": "Kelly",
  "age":25, 
  "salary": 8000, 
  "city": "New york" }

keys = ["name", "salary"]

dict1 = {id: dict[id] for id in keys}
print(dict1)


#Exercise 3*: Access the value of key ‘history’ from the below dict
dict = {
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
print(dict ['class']['student']['marks']['history'])
#question in 34 line

#Exercise 4*: Change Brad’s salary to 8500 from a given Python #dictionary
dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 6500}
}
dict['emp3']['salary'] = 8500
print(dict)









 
