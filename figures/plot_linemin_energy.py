import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("linemindata.csv", header=0)
plt.figure(figsize=(4, 2))
plt.errorbar(range(len(df)), df["energy"], df["energy_error"])
plt.xlabel("optimization step")
plt.ylabel("energy (Ha)")
plt.title("Si wave function optimization")
plt.savefig("linemin.pdf", bbox_inches="tight")
plt.show()
