"""
Local Variable: The variable declared within the function is called Local variable
                and it can be accessed within that function only.

Global variable: The variable declared outside of the function is called global variable and
                it can be accessed in any of the functions.
"""

age=25  #global variable

def display():
    x=20  # local variable
    print(x)
    print(age)

def show():
    #print(x)
    print(age)


display()
show()