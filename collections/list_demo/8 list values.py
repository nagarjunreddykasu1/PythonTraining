
emps=[[101,'Nagarjun',40000,'Hyderabad'],[103,'Prateek', 50000, 'Texas'],[102,'Geetha',60000,'Plano']]

print(emps, len(emps))

for p in emps:
    p.pop(3)

print(emps)  #[[101, 'Nagarjun', 40000], [103, 'Prateek', 50000], [102, 'Geetha', 60000]]

# Task: Extract only names and sort the names in ascending order
emps=[[101,'Nagarjun',40000,'Hyderabad'],[103,'Prateek', 50000, 'Texas'],[102,'Geetha',60000,'Plano']]

names=[]

for p in emps:
    names.append(p[1])

print(names) #['Nagarjun', 'Prateek', 'Geetha']
print(sorted(names)) #['Geetha', 'Nagarjun', 'Prateek']


