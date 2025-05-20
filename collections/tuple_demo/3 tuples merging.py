x=(10,20,30,40)

y=(50,60,70,80)

z= x+y
print(z, type(z), len(z)) #(10, 20, 30, 40, 50, 60, 70, 80) <class 'tuple'> 8

x="python"
print(x*3)

y=(10,20,30)
print(y*3) #(10, 20, 30, 10, 20, 30, 10, 20, 30)

print(y+3) #TypeError: can only concatenate tuple (not "int") to tuple
