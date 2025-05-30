#Tuple Packing and Unpacking

#Tuple packing: creating a tuple without paranthesis
marks=90,80,70
print(marks, type(marks)) #(90, 80, 70) <class 'tuple'>

#Tupe unpacking: Assigning a tuple to multiple variables
marks=(90,80,70)
s1,s2,s3=marks

print(s1, type(s1)) #90 <class 'int'>
print(s2, type(s2))
print(s3, type(s3))

