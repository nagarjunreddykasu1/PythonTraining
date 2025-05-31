
x=list()
print(x, type(x))

x=list("python")
print(x, type(x))  #['p', 'y', 't', 'h', 'o', 'n'] <class 'list'>

x=list("java")
print(x)

'''
x=list(10) #TypeError: 'int' object is not iterable
print(x, type(x))
'''

x=list([1,2,3])
print(x, type(x)) #[1, 2, 3] <class 'list'>