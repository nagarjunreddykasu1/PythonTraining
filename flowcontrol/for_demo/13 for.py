'''
A
BB
CCC
DDDD
EEEEE
FFFFFF
GGGGGGGG
HHHHHHHHH
IIIIIIIIII
'''

num=int(input("Enter a number: "))

for i in range(1,num+1):
    for j in range(1, i+1):
        print(chr(i+64),end="")
    print()


'''
A-65
B-66

a-97

'''