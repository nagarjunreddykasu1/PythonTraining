'''
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10

'''

num=int(input("Enter a number: "))
for i in range(1, num+1): #no. of rows
    for p in range(1,11): #no. of columns
        print(p, end=" ")
    print()
