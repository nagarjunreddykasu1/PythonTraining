x={10,20,30,40,50}

print(x, type(x), len(x))   #{50, 20, 40, 10, 30} <class 'set'> 5

y={"Python", 3.5, True, 100}
print(y, type(y), len(y))    #{'Python', True, 3.5, 100} <class 'set'> 4

z={10,20,30,(40,50,60)}
print(z, type(z), len(z))  #{10, (40, 50, 60), 20, 30} <class 'set'> 4

'''
p={10, [25,35]}  #TypeError: unhashable type: 'list'

p={{22,25}}

print(p)
'''
a=set()
print(a, type(a), len(a))

b=set("python")
print(b, type(b), len(b))    #{'n', 'y', 't', 'o', 'h', 'p'} <class 'set'> 6

'''
c=set("python","java")
print(c)   #TypeError: set expected at most 1 argument, got 2
'''

d=set([10,20,"Python", True, 3.5])
print(d)    #{True, 3.5, 10, 20, 'Python'}

e={(1,2,3,4,5)}

print(e, type(e),len(e))

dup={10,20,30,10,20,40}
print(dup)   #{40, 10, 20, 30}