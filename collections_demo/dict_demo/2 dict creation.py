from struct import pack_into

person={"sachin":90,"Ganguly":75,"Dravid":35}

print(person)
print(type(person))
print(len(person))

x={"height":5.7,30:"age"}
print(x)
print(type(x))
print(len(x))


details={"name":"Prateek", "age":25, "height":5.7}
print("========Accessing Values ============")
print(details["name"])
print(details["age"])
print(details["height"])
print("========Accessing Keys ============")
for p in details:
    print(p, type(p))

print("========Accessing Values using for loop ============")
for p in details:
    print(details[p])

print("========Accessing both Keys and Values ============")
'''
name:Prateek
age:25
city:Texas
'''
for p in details:
    print(p,":",details[p])