x=dict()
print(x)
print(type(x), len(x))

a={10,20,30}
print(a, type(a))

b={"a":10,"b":20,"c":30}
print(b,type(b),len(b))

c=dict(b)
print(c, type(c), len(c))

d=c
print(d)

players=dict([("age",20),("name","Prateek")])
print(players)

players=dict([{"age",20},{"name","Prateek"}])
print(players)

# In a dictionary, value can be of any type like int, float, string, bool, list, tuple,set, dictionary

x={"emps":["Prateek","Nagarjun","Geetha","Rahul"], "eid":[101,102,103,104]}
print(x, type(x),len(x))

print(x["emps"][0])
print(x["emps"][0:2])

