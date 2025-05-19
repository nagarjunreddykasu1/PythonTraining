#List methods

x=[10,20,30,40,50]
print(x, len(x))

#1. append(): To append an element at the end of list
x.append(60)
print(x, len(x))

#x.append(70,80) #TypeError: list.append() takes exactly one argument (2 given)

for p in [70,80,90]:
    x.append(p)

print(x, len(x)) #[10, 20, 30, 40, 50, 60, 70, 80, 90] 9

#2. extend(): Copy one list of elements into another list
y=[1.5,2.5,3.5]
x.extend(y)
print(x, len(x)) #[10, 20, 30, 40, 50, 60, 70, 80, 90, 1.5, 2.5, 3.5] 12

#3. insert(index, value): To insert an element at the desired location
#[10, 20, 30, 40, 50, 60, 70, 80, 90, 1.5, 2.5, 3.5]
x.insert(1, "python")
print(x, len(x)) #[10, 'python', 20, 30, 40, 50, 60, 70, 80, 90, 1.5, 2.5, 3.5] 13
