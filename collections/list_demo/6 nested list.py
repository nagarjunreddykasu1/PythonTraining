#Nested list: Lists within a list

x=[["Python", 30],["Java", 20],["AWS", 40]]

print(x, type(x))
print(len(x)) #3

for p in x:
    print(p, type(x))

for p,q in x:
    print("Course: ",p)
    print("Ranking: ",q)
    print("============================")