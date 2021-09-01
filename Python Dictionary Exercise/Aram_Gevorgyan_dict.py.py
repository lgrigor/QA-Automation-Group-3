keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
#x = dict(zip(('Ten', 'Twenty', 'Thirty'), (10, 20, 30)))
x = dict(zip((keys), (values)))
print(x)


sampleDict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
sampleDict.pop("age")
sampleDict.pop("city")
print(sampleDict)



sampleDict = {"class":{"student":{"name":"Mike","marks":{"physics":70,"history":80}}}}
print(sampleDict["class"] ["student"] ["marks"] ["history"])


sampleDict = {
'emp1': {'name': 'Jhon', 'salary': 7500},
'emp2': {'name': 'Emma', 'salary': 8000},
'emp3': {'name': 'Brad', 'salary': 6500}
}
sampleDict_1 = {'emp3':{'name': 'Brad', 'salary': 8500}}
sampleDict.update(sampleDict_1)
print(sampleDict)