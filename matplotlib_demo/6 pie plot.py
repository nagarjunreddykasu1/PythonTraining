import matplotlib.pyplot as plt

plt.title("Mobile Sales")

mobile_labels=['Samsung', 'Vivo', 'Oppo', 'OnePlus']

sales_may=[55,20,10,15]

plt.pie(sales_may,labels=mobile_labels)
plt.legend()
plt.show()


