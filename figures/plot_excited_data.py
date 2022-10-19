import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("original_excited_data.csv", header=0)
state = df["State"]
expt = df["Experiment"][:5].astype(float)
print(expt)
df = df[["DMC", "DMC err", "CC3"]].astype(float)

print(df)

plt.figure(figsize=(6, 4))
#plt.errorbar(range(len(df)), df["DMC"], df["DMC err"], ls="", c="orange")
size=100
plt.scatter(range(len(df)), df["CC3"], label=r"CC3$^2$", marker=(5, 1, 180), s=size, )
plt.scatter(range(len(df)), df["DMC"], label=r"DMC $\vec{\alpha}, \vec{c}, \vec{\beta}$", marker=(5, 1, 0), s=size, )
plt.scatter(range(len(expt)), expt, label=r"Expt.$^{3-7}$", marker=".", s=size, edgecolors="k")
plt.xticks(range(len(df)), state)
plt.ylabel("Energy (eV)")
plt.xlabel("electronic state")
plt.title("Benzene excited states")
plt.ylim([3.9, 10])
plt.legend()
plt.savefig("excited_states_plot.pdf", bbox_inches="tight")
plt.show()
