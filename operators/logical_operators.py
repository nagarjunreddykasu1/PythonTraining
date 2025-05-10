'''
Logical Operators:

1. and
2. or
3. not

x       y       x and y     x or y
True    True    True        True
True    False   False       True
False   True    False       True
False   False   False       False


logical and returns True only of both the conditions are True else it returns False
Logical or returns True if both the conditions are True or if any one condition is True.
'''

x=10
y=20
z=30

p = (x>y) and (z>y)
print(p)

p = (x>y) or (z>y)
print(p)

q = (x>y) and (z>y) or (x!=z)
print(q)

print(not False)
print(not True)