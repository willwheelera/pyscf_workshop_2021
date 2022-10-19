import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return 0.1 / (1.1 - x) + .05

# Generate curve data
x = np.linspace(0.1, 1, 100)
y = func(x)

# Format axes
fig, ax = plt.subplots(1, 1, figsize=(3,3))
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.set_xticks([])
ax.set_yticks([])
ax.set_ylim([0, 1.1])

# Plot curve
ax.plot(x, y)
ax.set_xlabel("accuracy")
ax.set_ylabel("computational cost")

# Plot points
x = [0.3, 0.35, 0.6, 0.7, 0.79, 0.82, .91, .915, .92]
methods = ["HF", "DFT", "MP2", "VMC", "CCSD", "DMC", "SHCI", "CCSD(T)", "DMRG"]
xshift = [-.05, -0.05, -.05, 0.0, -.08, .10, .05, .05, .05]
yshift = [0.05, -0.12, -0.12, -0.12, .05, -.05, -.08, -.03, .02]
for i, method in enumerate(methods): 
    y = func(x[i])
    if method == "HF" or method=="CCSD":
        y += .10
    ax.scatter(x[i], y, s=180, marker="o", alpha=0.6, edgecolor="")
    c = {}
    if method=="DMC":
        color = "#99FF22"
        ax.scatter(x[i], y, s=220, marker="o", facecolor="", lw=3, edgecolor=color)
        c = {"backgroundcolor": color, "fontweight": "bold"}
    ax.text(x[i] + xshift[i], y+yshift[i], method, **c)

plt.title("    Electronic structure methods")
plt.savefig("pareto.pdf", bbox_inches="tight")
#plt.show()
