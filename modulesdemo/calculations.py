
age=30
name="Nagarjun"


def add():
    x=int(input("Enter value of x:"))
    y=int(input("Enter value of y:"))
    z=x+y
    print("SUM: ",z)

def table():
    num=int(input("Enter a number:"))
    for i in range(1,11):
        print(f"{num} X {i} = {num * i}")

def even_odd():
    num=int(input("Enter a Number:"))
    if num % 2 == 0:
        print(f"{num} is even number")
    else:
        print(f"{num} is Odd number")
