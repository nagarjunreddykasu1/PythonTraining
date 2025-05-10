'''
Identity Operators: are used to compare the addresses of 2 objects
1. is
2. is not


'''
x=10
y=20
print(x, id(x))
print(y, id(y))
print(x is y) #compares the address
print(x is not y)

print(x==y) #compares the content

a=10
b=10
print(a, id(a))
print(b, id(b))
print(a is b)
print(a==b)

x=[10,20,30]
y=[10,20,30]
print(x, id(x))
print(y, id(y))
print(x is y)
print(x==y)