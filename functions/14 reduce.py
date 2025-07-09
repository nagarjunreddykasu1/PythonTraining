"""
reduce():
It reduces the iterable to a single cumulative value.

reduce() takes 2 arguments:
    1. lambda function
    2. iterable type

syntax:
reduce(lambda_function, iterable_type)

we need to import reduce from functools module
"""
from functools import reduce

list1=[1,2,3,4,5,6]
# task is to sum all numbers from the list

resul1=reduce(lambda x,y:x+y, list1)
# (1+2),3,4,5,6
# 6,4,5,6
# 10, 5,6
#15,6
# 21
print(resul1)

# to find the largest number
result2 = reduce(lambda x,y: x if x>y else y,list1)
print(result2)

#to find the longest word from the list of strings
words=["python", "developer", "ai", "automation"]
longest = reduce(lambda x,y: x if len(x)>len(y) else y,words)
print(longest)

# to concatenate strings
contact_string = reduce(lambda x,y:x+" "+y,words)
print(contact_string)

# python developer ai automation


