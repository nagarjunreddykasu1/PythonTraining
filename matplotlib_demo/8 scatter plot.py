import matplotlib.pyplot as plt

months=[1,2,3,4,5,6]
sales=[20,15,25,40,30,35]

plt.scatter(months,sales,label='Moble Sales',color='green', marker='o')

plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Mobile Sales Analysis')
plt.grid()
plt.legend()
plt.show()
