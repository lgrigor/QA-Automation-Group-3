"""Python Dictionary Exercise"""
# Exercise 1: Below are the two lists convert it into the dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dict_1 = dict(zip(keys, values))
print(dict_1)

# Exercise 2: Create a new dictionary with the following keys from a below dictionary
sampleDict = {
       "name": "Kelly",
       "age":25,
       "salary": 8000,
       "city": "New york"
}


new_dict = {}
new_dict['name'] = sampleDict['name']
new_dict['age'] = sampleDict['age']
print(new_dict)

# Exercise 3*: Access the value of key ‘history’ from the below dict
sampleDict = {
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
print(sampleDict['class']['student']['marks']['history'])

# Exercise 4*: Change Brad’s salary to 8500 from a given Python dictionary
sampleDict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 6500}
}

sampleDict['emp3']['salary'] = 8500
print(sampleDict)