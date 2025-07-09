"""
Arbitrary arguments or variable length arguments:

we can specify more no' of argument values during function call.

An asterisk (*) is placed before the argument name that holds multiple values


"""


def display(name, *marks):
    print(marks, type(marks))
    print(name, type(name))
    for p in marks:
        print(p)


display("Nagarjun", 55, 70, 80, 90, 63, 85)


def display(**details):
    print(details, type(details))
    for k, v in details.items():
        print(k, v)


display(cid=122, name="Nagarjun", bal=54343, city="Hyderabad")
