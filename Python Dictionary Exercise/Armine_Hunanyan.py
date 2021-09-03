Dictionary

Ex1:
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dictionary = dict(zip(keys, values))
print(dictionary) 


Ex4:
sampleDict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 6500}
}
sampleDict['emp3']['salary'] = 8500
print(sampleDict)
 

Ex:3
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



Ex2:
sampleDict = {
       "name": "Kelly",
       "age":25,
       "salary": "8000",
       "city": "New york"
}
Keys = ["name", "salary"]
 
newDict = {"name": sampleDict["name"], "salary": sampleDict["salary"]}
print(newDict)
 


