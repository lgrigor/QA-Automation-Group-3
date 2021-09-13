keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
x=(dict(zip(keys,values)))
print(x)



sampleDict = {
       "name": "Kelly",
       "age":25,
       "salary": 8000,
       "city": "New york"
}
keys = ["name","salary"]
y = {x: sampleDict[x] for x in keys}
print (y)



x = {
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

z=x["class"]["student"]["marks"]["history"]
print(z)



sampleDict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 6500}
}
sampleDict['emp3']['salary']=8500
print(sampleDict)
