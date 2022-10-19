import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys

fname = "results.csv"

df = pd.read_csv(fname, header=0)
nelec = {
  "benzene": 30, 
  "anthracene": 66,
  "coronene": 108,
  "ovalene": 142,
  "hexabenzocoronene": 186,
}
df["nelec"] = [nelec[s] for s in df["system"]]
df["loc"] = ["gpu" if g else "cpu" for g in df["gpu"]]
#print(df)

df.sort_values("nelec", inplace=True)
g = sns.FacetGrid(data=df, hue="loc", height=3, legend_out=False)
g.map(plt.plot, "nelec", "time", marker="o")
g.add_legend()
#sns.barplot(x="nelec", y="time", hue="loc", data=df)
g.legend.set_title("")
plt.savefig("gpuplot.pdf", bbox_inches="tight")
plt.show()
