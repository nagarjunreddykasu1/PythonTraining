import matplotlib.pyplot as plt

lg_x=[1,3,5,7,9]
lg_y=[9,3,7,5,6]
plt.bar(lg_x, lg_y,label="LG",color="blue",width=0.9)

plt.bar([2,4,6,8,10],[5,9,5,2,4],label="Sony",color="g",width=0.7)

plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Product Sales")
plt.legend()

plt.show()