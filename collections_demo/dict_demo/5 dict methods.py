employee={"name":"Nagarjun", "salary":57000, "designation":"Team Lead", "location":"Hyderabad"}

print(employee.keys())
print(employee.values())
print(employee.items())

print(employee["name"])  #KeyError: 'name1' if the specified key is not available in the dictionary
print(employee.get("name11", "Prateek")) # returns None if the specified key is not available, we can add default value as second parameter

employee.pop("location")
print(employee) #{'name': 'Nagarjun', 'salary': 57000, 'designation': 'Team Lead'}

employee.popitem() # it randomly removes an item
print(employee)

employee.clear()
print(employee, len(employee))