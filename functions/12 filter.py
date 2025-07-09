"""
filter(): The filter() is used to filter data from an iterable based on a condition

filter function takes 2 arguments:
    1. lambda function
    2. iterable type like string, list, tuple, set, dict

syntax:
filter(lambda_function, iterable)

"""

#ex: task us filter the values with >20
list1 = [10,20,30,40,50]
result1 = list(filter(lambda x: x>20, list1))
print(result1)

#ex2:
emps = [
    [101,'Nagarjun',55000,'m',11,'Hyderabad'],
    [102,'Prateek',45000,'m',14,'Texas'],
    [101,'Geetha',65000,'f',13,'Dallas'],
    [101,'Rajesh',22500,'m',11,'Hyderabad']
]

# task is to filter the emps who belong to Hyderabad
hyd_emps = list(filter(lambda x: x[5]=='Hyderabad', emps))
print(hyd_emps)

# task is to filter only male emp records
male_emps = list(filter(lambda x:x[3]=='m', emps))
print(male_emps)

# task is to filter the emps whose salary is > 50000
result2 = list(filter(lambda x:x[2] > 50000, emps))
print(result2)
