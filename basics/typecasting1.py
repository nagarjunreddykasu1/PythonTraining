#Typecasting: Converting one datatype to another datatype

# For typecasting -> we have functions -> int(), float(), str(), bool()

#case1: Converting a string to int
x="100"
print(type(x))
y = int(x)
print(y, type(y))

'''
name = "Nagarjun"
print(name, type(name))
na = int(name)
print(na, type(na))
'''

#Case2: Converting a int to string
x = 100
print(x, type(x))

y = str(x)
print(y, type(y))
#print(y+25) #TypeError: can only concatenate str (not "int") to str

#Case 3: Converting a int to float
x = 20
print(x, type(x))
y= float(x)
print(y, type(y))

# case 4: Converting float to int
x = 4.9
print(x, type(x))
y = int(x)
print(y, type(y))

#Case5:  Converting int to bool (True/False)
x = 0.00
print(x, type(x))
y = bool(x)
print(y, type(y))

#Case6: Converting bool to int
x = False
print(x, type(x))
y=int(x)
print(y, type(y))