def add():
    x=int(input("Enter value of x:"))
    y=int(input("Enter value of y:"))
    z=x+y
    print("SUM: ",z)


add()
add()

"""
1. define a function to print table based on given number
2. define a function to check whether the given number is even or odd

"""
def table():
    num=int(input("Enter a number:"))
    for i in range(1,11):
        print(f"{num} X {i} = {num * i}")


table()
table()
