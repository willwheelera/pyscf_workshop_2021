import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

jastrow = "jastrow"
ewald = "ewald"
mos = "MOs"
evalgto = "eval_gto"
asarray="asarray"
einsum="einsum"
ecp="other ecp"
Si1 = "Si 8-atom"
Si2 = "Si 64-atom"
benzene = "benzene molecule"
coronene = "coronene molecule"
profile_data = []
profile_data.append(dict(system=Si1, part=evalgto, percent=61.34))
profile_data.append(dict(system=Si1, part=jastrow, percent=15.43))
profile_data.append(dict(system=Si1, part=mos,     percent=2.34))
profile_data.append(dict(system=Si1, part=asarray, percent=2.89))
profile_data.append(dict(system=Si1, part=einsum,  percent=4.77))
profile_data.append(dict(system=Si1, part=ecp,     percent=1.50))
profile_data.append(dict(system=Si1, part=ewald,   percent=10.5))
profile_data.append(dict(system=Si2, part=evalgto, percent=52.81))
profile_data.append(dict(system=Si2, part=jastrow, percent=17.59))
profile_data.append(dict(system=Si2, part=mos,     percent=4.36))
profile_data.append(dict(system=Si2, part=asarray, percent=2.17))
profile_data.append(dict(system=Si2, part=einsum,  percent=5.57))
profile_data.append(dict(system=Si2, part=ecp,     percent=5.98))
profile_data.append(dict(system=Si2, part=ewald,   percent=6.47))
profile_data.append(dict(system=benzene, part=evalgto, percent=18.53))
profile_data.append(dict(system=benzene, part=jastrow, percent=50.92))
profile_data.append(dict(system=benzene, part=mos,     percent=15.19))
profile_data.append(dict(system=benzene, part=asarray, percent=2.55))
profile_data.append(dict(system=benzene, part=einsum,  percent=3.70))
profile_data.append(dict(system=benzene, part=ecp,     percent=5.78))
profile_data.append(dict(system=coronene, part=evalgto, percent=17.38))
profile_data.append(dict(system=coronene, part=jastrow, percent=41.80))
profile_data.append(dict(system=coronene, part=mos,     percent=28.30))
profile_data.append(dict(system=coronene, part=asarray, percent=1.92))
profile_data.append(dict(system=coronene, part=einsum,  percent=3.51))
profile_data.append(dict(system=coronene, part=ecp,     percent=4.20))
df = pd.DataFrame(profile_data)

for k, v in dict(Si1=Si1, Si2=Si2, benzene=benzene, coronene=coronene).items():
    d = df[df["system"]==v]
    percent = d["percent"].sum()
    d.append(dict(system=v, part="other", percent=percent), ignore_index=True)
    print(percent)
    print(d)
    plt.figure(figsize=((3, 3)))
    plt.pie(d["percent"]/100, labels=d["part"], autopct="%.0f%%", colors=sns.color_palette("Set3"), pctdistance=0.8, normalize=False, startangle=60)
    plt.title(v)
    plt.savefig(f"profile_{k}.pdf", bbox_inches="tight")
    plt.show()

