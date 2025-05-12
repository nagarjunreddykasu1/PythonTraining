'''
1. if
2. if-else


syntax:
if condition:
    st1
    st2
    st3 (block1)
    st4
else:
    st5
    st6  (block2)
    st7

if condition is True then the statements within the if block (block1) will be executed.
if condition is False then the statements within the else block (block2) will be executed.
'''

x=int(input("Enter the value of x: "))
y=int(input("Enter the value of y: "))

if x==y:
    print("Both the numbers are equal.")
else:
    print("Both the numbers are not equal....")