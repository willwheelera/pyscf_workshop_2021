import numpy as np
import matplotlib.pyplot as plt
import h5py
import pyqmc

with h5py.File("redo_si_example.dmc.hdf", "r") as hdf:
    energy = np.array(hdf["energytotal"])

warmup = 60
rb = pyqmc.reblock.reblock(energy[warmup:], 40)
mean = rb.mean()
err = rb.std() / np.sqrt(len(rb) - 1)

plt.figure(figsize=(4, 2))
plt.plot(np.arange(len(energy)) * 5, energy)
x0, x1 = plt.xlim()
color="green"
rect = plt.Rectangle([x0, mean - err], x1-x0, 2 * err, alpha=.3,
                             facecolor=color, edgecolor=None)
plt.gca().add_patch(rect)
plt.xlabel("DMC step")
plt.ylabel("E (Ha)")
plt.title("DMC energy")
plt.savefig("dmc.pdf", bbox_inches="tight")
plt.show()
