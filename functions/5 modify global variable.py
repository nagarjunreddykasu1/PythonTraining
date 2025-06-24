

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
