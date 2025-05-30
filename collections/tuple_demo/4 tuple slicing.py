#Tuple slicing

x=("Amar","Rohith","Rahul","Blake","James","Miller")

print(x[3])
print(x[-3])

print(x[0:3]) #('Amar', 'Rohith', 'Rahul')
print(x[2:]) #('Rahul', 'Blake', 'James', 'Miller')
print(x[-4:]) #('Rahul', 'Blake', 'James', 'Miller')

print(x[:]) #('Amar', 'Rohith', 'Rahul', 'Blake', 'James', 'Miller')
print(x[0:6:2]) #('Amar', 'Rahul', 'James')
print(x[::2]) #('Amar', 'Rahul', 'James')

print(x[::-1]) #('Miller', 'James', 'Blake', 'Rahul', 'Rohith', 'Amar')
