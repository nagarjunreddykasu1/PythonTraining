"""
Types of Functions:
Lambda functions
Filter function
map function
reduce function
recursive function
"""

"""
1. Lambda function: A function without any name is called lambda function

used for simple operations.

syntax:
lambda arguments:expression

we can specify multiple arguments within the lambda function, but only one expression
"""


def square(x):
    print(x**2)

square(10)

sq1 = lambda x : x**2
print(sq1(20))
print(type(sq1))
print(sq1(12))

# ex: 2
mult = lambda x, y : x*y

print(mult(5,10))

# ex: 3
s = lambda x, *y:sum(y)
print(s(10,2,3,4))

# ex; 4
to_upper = lambda s:s.upper()
print(to_upper("nagarjun"))

# ex: 5
reverse_string = lambda s : s[::-1]
print(reverse_string("prateek"))



