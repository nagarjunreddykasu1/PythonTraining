

age=25  #global variable

def display():
    global age
    x=10 #local variable
    age=30
    print(x)
    print(age)

def show():
    print(age)

display()
show()


"""
Types of arguments:
1. Non-default arguments or positional arguments
2. Default arguments
3. Keyword argument
4. Non-keyword argument
5. Arbitrary or variable length arguments

"""