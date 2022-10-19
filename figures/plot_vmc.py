import numpy as np
import matplotlib.pyplot as plt
import h5py
import pyqmc

with h5py.File("redo_si_example.vmc.hdf", "r") as hdf:
    energy = np.array(hdf["energytotal"])

warmup = 20
rb = pyqmc.reblock.reblock(energy[warmup:], 40)
mean = rb.mean()
err = rb.std() / np.sqrt(len(rb) - 1)

plt.figure(figsize=(4, 2))
plt.plot(np.arange(len(energy)) * 10, energy)
x0, x1 = plt.xlim()
color="green"
rect = plt.Rectangle([x0, mean - err], x1-x0, 2 * err, alpha=.3,
                             facecolor=color, edgecolor=None)
plt.gca().add_patch(rect)
plt.xlabel("VMC step")
plt.ylabel("E (Ha)")
plt.title("VMC energy")
plt.savefig("vmc.pdf", bbox_inches="tight")
plt.show()
