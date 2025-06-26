"""
1. Non-keyword arguments: During function call, passing value without parameter name(keyword)

2. keyword arguments: During function call, passing value with parameter names

Note:
After keyword arguments, we can not specify non-keyword arguments
but after non-keyword arguments, we can specify keyword arguments

"""

def customer(cid, cname, bal, city):
    print(cid, cname, bal, city)


customer(101, "Nagarjun", 55000, "Hyderabad") # non-keyword arguments

customer(cid=123, cname="Prateek", bal=77000, city="Dallas") #keyword argument

customer(cname="Prateek", city="Dallas", bal=77000, cid=123) #keyword argument

customer(111, "Geetha", bal=97000, city="Texas")

# customer(cid=111, cname="Geetha", 97000, "Texas") #error: Positional argument after keyword argument