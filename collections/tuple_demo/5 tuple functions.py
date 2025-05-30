x=(30,10,40,20,50)

print(type(x))
print(len(x)) #5
print(sum(x)) #150
print(max(x))
print(min(x))

print(sorted(x)) #[10, 20, 30, 40, 50]
print(sorted(x,reverse=True)) #[50, 40, 30, 20, 10]
print(x[::-1]) #(50, 20, 40, 10, 30)

print(sorted(x[::-1])) #[10, 20, 30, 40, 50]
print(sorted(x[::-1],reverse=True)) #[50, 40, 30, 20, 10]

print(reversed(x)) #<reversed object at 0x0000020EE6A650F0>

for p in reversed(x):
    print(p,end=" ") #50 20 40 10 30

print()
for p in reversed(sorted(x)):
    print(p, end=" ")  #50 40 30 20 10
print()

x=("Lion","Tiger", "Elephant", 'cat')
print(max(x)) #cat
print(min(x)) #Elephant
print(sorted(x))  #['Elephant', 'Lion', 'Tiger', 'cat']
'''
A-65
B-66

Z-90

a-97
b-98
c-99

'''