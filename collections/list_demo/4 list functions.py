x=[50,10,30,20,40]

print(x)
print(len(x))

print(sum(x))
print(max(x)) #50
print(min(x)) #10

print(sorted(x)) #[10, 20, 30, 40, 50]

print(sorted(x, reverse=True)) #[50, 40, 30, 20, 10]

print(reversed(x)) #<list_reverseiterator object at 0x0000025076634F70>

for p in reversed(x):
    print(p, end=" ")  #40 20 30 10 50
print()

for p in reversed(sorted(x)):
    print(p, end=" ") #50 40 30 20 10

