Exercise 1:
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
newDict = dict(zip(('Ten', 'Twenty', 'Thirty'), (10, 20, 30)))
print(newDict)

Exercise 2:

sampleDict = {
       "name": "Kelly",
       "age":25,
       "salary": 8000,
       "city": "New york"
}
nameValue = sampleDict.get("name")
salaryPrice = sampleDict.get("salary")
newDict = dict()
newDict["name"] = nameValue
newDict["salary"] = salaryPrice
print(newDict)

Exercise 3:
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

newDict= sampleDict.get("class").get("student").get("marks").get("history")
print(newDict)


Exercise 4:
sampleDict = {
   'emp1': {'name': 'Jhon', 'salary': 7500},
   'emp2': {'name': 'Emma', 'salary': 8000},
   'emp3': {'name': 'Brad', 'salary': 6500}
}
sampleDict.get("emp3").update({"salary": 8500})
print(sampleDict)

