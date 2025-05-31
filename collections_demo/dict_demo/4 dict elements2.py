person={"name":"Prateek", "age":25, "height":5.7}

person["age"]=27
person["weight"]=80

print(person) #{'name': 'Prateek', 'age': 27, 'height': 5.7, 'weight': 80}

employee={"name":"Nagarjun", "salary":57000, "designation":"Team Lead", "location":"Hyderabad"}

print(employee["name"])

print("==== Access all Keys ======")
for key in employee:
    print(key)

print("==== Access all the values ======")
for key in employee:
    print(employee[key])