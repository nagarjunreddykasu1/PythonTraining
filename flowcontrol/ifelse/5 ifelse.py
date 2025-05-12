'''
nested block:
block within a block

if condition:
    st1
    st2
    if condition:
        st3
        st4
    else:
        st5
        st6
    st9
    st10
else:
    st7
    st8

'''

x=int(input("Enter value of x: "))
y=int(input("Enter value of y: "))
z=int(input("Enter value of z: "))

if x>y:
    if x>z:
        print(x,"is the largest")
    else:
        print(z, "is the largest")
else:
    if y>z:
        print(y, "is the largest")
    else:
        print(z, "is the largest")