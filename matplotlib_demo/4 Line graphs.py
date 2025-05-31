import matplotlib.pyplot as plt
from matplotlib.lines import lineStyles

overs=[10,20,30,40,50]
runs_india=[75,110,195,230,290]
runs_pak=[50,95,155,205,260]

plt.plot(overs, runs_india,color="blue",marker="o",label="INDIA")

plt.plot(overs,runs_pak,color="green",linestyle="dashed",linewidth="2",label="PAKISTAN")
plt.grid()
plt.xlabel("OVERS")
plt.ylabel("RUNS")
plt.title("SCORE COMPARISONS")
plt.legend()

plt.show()


