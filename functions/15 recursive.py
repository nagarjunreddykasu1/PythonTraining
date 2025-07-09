"""
Recursive function: A function which is called by itself is known as recursive function

"""
x=1  # global variable
def recursive():

    global x
    while x<=5:
        print("python")
        x=x+1  #2  3  4 5 6
        recursive()



recursive()

