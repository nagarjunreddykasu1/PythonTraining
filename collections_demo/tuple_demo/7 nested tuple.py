# Nested Tuple: tuple within a tuple

x=(("Kohli",96),("Rohith",55),("Dhoni",45))

print(x, type(x), len(x))

for p in x:
    print(p,type(p))

for p,q in x:
    print("PLAYER:",p)
    print("RUNS:",q)
    print("==============================")

emps=((101,"Miller",45000,"Manager"),
      (103,"Prateek", 55000, "Lead"),
      (102, "Nagarjun",43000, "Associate Manager"),
      (104,"Geetha", 56000, "Team Lead"))

print(emps, type(emps))

for p in emps:
    print(p,type(p))

for p,q,r,s in emps:
    print("EID:",p)
    print("ENAME:",q)
    print("ESAL:",r)
    print("ETITLE:",s)
    print("=======================")





