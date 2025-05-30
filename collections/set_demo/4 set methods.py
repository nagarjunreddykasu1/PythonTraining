# set methods

x={10,20,30,40,50}
print(x)

x.add(65)
#x.add(75,78)  #TypeError: set.add() takes exactly one argument (2 given)
print(x)

#x.add((3.5,4.5,5.5))
#print(x)    #{65, 50, 20, (3.5, 4.5, 5.5), 40, 10, 30}

#{65, 50, 20, 3.5, 4.5, 5.5, 40, 10, 30}

for p in (3.5,4.5,5.5):
    x.add(p)

print(x)   #{65, 3.5, 4.5, 5.5, 10, 20, 30, 40, 50}

#update(): To insert multiple elements at a time
x.update((11,22,33))   #{65, 3.5, 4.5, 5.5, 10, 11, 20, 22, 30, 33, 40, 50}
print(x, len(x))

#pop(): removes an element randomly
x.pop()
x.pop()
print(x, len(x))

#discard(): removes a particular element
x.discard(3.5)
print(x)   #{4.5, 5.5, 10, 11, 20, 22, 30, 33, 40, 50}

x.discard(99)
print(x)

# remove():
x.remove(4.5)
print(x)   #{5.5, 10, 11, 20, 22, 30, 33, 40, 50}

'''
x.remove(99)
print(x)    #KeyError: 99
'''

#clear():
x.clear()
print(x, len(x))
