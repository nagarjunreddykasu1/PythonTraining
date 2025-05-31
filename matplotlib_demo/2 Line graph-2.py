import matplotlib.pyplot as plt

age=[25,30,35,40,45,50]
income=[30000,40000,50000,45000,70000,80000]

plt.plot(age, income,"--",color="green")
plt.xlabel("AGE")
plt.ylabel("INCOME")
plt.title("Line Graph with Income Comparison")

plt.show()