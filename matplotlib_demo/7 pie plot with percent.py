import matplotlib.pyplot as plt

activities=['sleeping', 'eating', 'working','playing']
hours = [8,2,8,6]
cols=['green','yellow','red','blue']

plt.pie(hours,labels=activities,colors=cols,shadow=True, explode=(0,0.2,0,0),autopct='%1.2f%%')

plt.title("Daily Activities")

plt.show()

