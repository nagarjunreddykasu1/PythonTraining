"""
map(): the map function is used to transform each element of iterable

apply a function to each item in iterable (list, tuple, set, dict)

map() takes 2 arguments:
    1. lambda function
    2. iterable

syntax:
map(lambda_function, iterable)

"""
# ex:
list1 = [10,20,30,40,50]
#task is to add 5 to each element of the list
result1 = list(map(lambda x: x+5, list1))
print(result1)

#ex2:
emps = [
    [101,'Nagarjun',55000,'m',11,'Hyderabad'],
    [102,'Prateek',45000,'m',14,'Texas'],
    [101,'Geetha',65000,'f',13,'Dallas'],
    [101,'Rajesh',22500,'m',11,'Hyderabad']
]

# task is to add 5000 to the salary of each employee as bonus

result2 = list(map(lambda x: [x[0],x[1], x[2]+5000,x[3],x[4],x[5]],emps))
print(result2)

# task is to update the gender m -> male f-> female

result3 = list(map(lambda x: [x[0], x[1], x[2], "male" if (x[3]=='m') else "female", x[4], x[5]],emps))
print(result3)


names = ["nagarjun","prateek","geetha"]

# convert to upper case
result4 = list(map(lambda x:x.upper(), names))
print(result4)

# length of each name
name_length = list(map(lambda x: len(x),names))
print(name_length)












