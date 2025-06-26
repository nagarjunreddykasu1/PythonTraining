"""
1. Non-default arguments: arguments specified in the function definition and
we must have to pass the values while calling the function

2. Default arguments: Arguments specified in the function with some default values.
It is not mandatory to pass the values during the function call.

"""

def display(name, age):
    print(name, age)


display("Nagarjun", 35)

def details(name="Prateek", age=24, address="USA"):
    print(name,age,address)

details()
details("Nagarjun", 30, "India")