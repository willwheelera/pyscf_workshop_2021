import matplotlib.pyplot as plt
import pandas as pd

df = {
"fname":
[
"accumulators.py", 
"coord.py",
"cvmc.py",
"distance.py",
"dmc.py",
"energy.py",
"eval_ecp.py",
"ewald.py",
"func3d.py",
"hdftools.py",
"__init__.py",
"jastrowspin.py",
"linemin.py",
"manybody_jastrow.py",
"mc.py",
"multiplywf.py",
"multislaterpbc.py",
"multislater.py",
"obdm.py",
"optimize_ortho.py",
"optvariance.py",
"pbc.py",
"reblock.py",
"recipes.py",
"slater.py",
"supercell.py",
"tbdm.py",
"testwf.py",
],
"nlines":
[
   226,
   199,
   372,
   131,
   410,
    76,
   208,
   402,
   483,
    43,
   321,
   385,
   307,
   210,
   256,
   124,
   325,
   371,
   256,
   704,
    54,
    27,
   166,
   222,
   330,
    68,
   282,
   220,
]
}

df = pd.DataFrame(df)
print(df)
df.sort_values("nlines", inplace=True)
df.plot.barh(x="fname", y="nlines", figsize=(3, 5), legend=False)
plt.title("total lines: %i"%df["nlines"].sum())
plt.xlabel("nlines")
plt.ylabel("")
plt.savefig("codelength.pdf", bbox_inches="tight")
plt.show()
