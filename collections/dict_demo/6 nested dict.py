#Nested dictionary: Dictionary within a dictionary

employee={"name":"Nagarjun", "salary":57000, "designation":"Team Lead", "location":{
    "address":"123 parkway",
    "city":"Dallas",
    "state":"Texas",
    "country":"USA"
}}

print(len(employee))

print(employee["designation"])
print(employee["location"])  #{'address': '123 parkway', 'city': 'Dallas', 'state': 'Texas', 'country': 'USA'}

print(employee["location"]["city"]) #Dallas
print(employee["location"]["address"]) #123 parkway

print(employee.keys())

print(employee.items())

"""
key -> value
name -> Nagarjun
salary -> 57000
designation -> Team Lead
location -> {'address': '123 parkway', 'city': 'Dallas', 'state': 'Texas', 'country': 'USA'}
"""
for key, value in employee.items():
    print(f"{key} -> {value}")


employee={"name":"Nag", "location":"Hyd", "name":"Nag"}
print(employee)