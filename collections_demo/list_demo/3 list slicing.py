# List slicing

x=[10,20,30,40,50]

print(x[0:3])  #upperbound is excluded

print(x[2:5]) #[30, 40, 50]

print(x[-3:])  #[30, 40, 50]
print(x[-3:-1]) #[30, 40]

print(x[:]) #[10, 20, 30, 40, 50] print(x)

print(x[0:5:2]) #[10, 30, 50]

print(x[0:4:2]) #[10, 30]

print(x[::-1]) #[50, 40, 30, 20, 10]
