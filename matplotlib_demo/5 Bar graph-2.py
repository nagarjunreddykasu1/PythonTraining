import matplotlib.pyplot as plt

parties=["Congress","BJP","TRS","MIM","CPI"]
votes=[64,10,34,2,7]

plt.bar(parties, votes, color=["red","green","magenta","blue","orange"])
plt.xlabel("Party")
plt.ylabel("No of Votes")
plt.title("ELECTIONS 2023")

plt.show()