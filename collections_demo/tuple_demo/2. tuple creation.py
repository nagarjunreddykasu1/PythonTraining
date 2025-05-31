from pyasn1_modules.rfc2985 import countryOfResidence

x=(10,20,30,40,50) # homogeneous

print(x, type(x), len(x))

y=(101, 'python', 15.55, True) # heterogeneous
print(y, type(y), len(y))

courses=('python') # if there is only one element within a tuple then it is not a tuple
print(courses, type(courses), len(courses))

courses=('python',)
print(courses, type(courses), len(courses)) #('python',) <class 'tuple'> 1

x=(10)
print(x, type(x))

x=([10,20], [30,40])
print(x, type(x), len(x))

x=tuple("Hyderabad")
print(x, type(x), len(x))

'''
x=tuple("Hyderabad","USA") #TypeError: tuple expected at most 1 argument, got 2
print(x, type(x), len(x))
#tuple() accepts only one argument that should be of iterable type like string, list, tuple, set


x=tuple(40)  #TypeError: 'int' object is not iterable
print(x, type(x))
'''
x=tuple((10,20,30))
print(x, type(x), len(x)) #(10, 20, 30) <class 'tuple'> 3

x=tuple([10,'Nag', 25.75, True])
print(x, type(x), len(x)) #(10, 'Nag', 25.75, True) <class 'tuple'> 4