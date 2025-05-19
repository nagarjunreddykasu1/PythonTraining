'''
1.

A A A A A A A A A A
B B B B B B B B B
C C C C C C C C
D D D D D D D
E E E E E E
F F F F F
G G G G
H H H
I I
J

2.
987654321
98765432
9876543
987654
98765
9876
987
98
9

'''

#=============================================================================
'''
A A A A A A A A A A
B B B B B B B B B
C C C C C C C C
D D D D D D D
E E E E E E
F F F F F
G G G G
H H H
I I
J
'''
for i in range(1,11):
    for j in range(1,12-i):
        print(chr(64+i),end=" ")
    print()
#=================================================================================
'''
A B C D E F G H I J 
A B C D E F G H I 
A B C D E F G H 
A B C D E F G 
A B C D E F 
A B C D E 
A B C D 
A B C 
A B 
A 
'''
for i in range(1,11):
    for j in range(1,12-i):
        print(chr(64+j), end=" ")
    print()

#=================================================================================
'''
987654321
98765432
9876543
987654
98765
9876
987
98
9
'''
for i in range(1,10):
    for j in range(1,11-i):
        print(10-j,end="")
    print()
#========================================================================================
'''
9 9 9 9 9 9 9 9 9 
8 8 8 8 8 8 8 8 
7 7 7 7 7 7 7 
6 6 6 6 6 6 
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1
'''
for i in range(1,10):
    for j in range(1,11-i):
        print(10-i,end=" ")
    print()

# https://github.com/gkolli2025/PythonTraining/tree/main/Practices