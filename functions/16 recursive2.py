"""
fact(5): 5*4*3*2*1 = 120
"""

def fact(n):
    if n==1:
        return 1
    else:
        return n * fact(n-1)

"""
5*fact(4)
5*4*fact(3)
5*4*3*fact(2)
5*4*3*2*1 = 120
"""



num = int(input("enter a number: "))
result = fact(num)
print("Factorial of", num, "is", result)