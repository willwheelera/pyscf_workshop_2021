import matplotlib.pyplot as plt
import pandas as pd
import h5py
import numpy as np


def plot_linemin():
    fname = "optbenzene.hdf5"
    with h5py.File(fname, "r") as hdf:
        energy = np.array(hdf["energy"])
        energy_error = np.array(hdf["energy_error"])

    plt.figure(figsize=(4, 2))
    plt.errorbar(range(len(energy)), energy, energy_error)
    plt.xlabel("optimization step")
    plt.ylabel("energy (Ha)")
    plt.title(r"Benzene wave function optimization")
    plt.savefig("benzene_linemin.pdf", bbox_inches="tight")


def rb_summary(energy, warmup, nblocks):
    import pyqmc.reblock
    rb = pyqmc.reblock.reblock(energy[warmup:], nblocks)
    mean = rb.mean(axis=0)
    err = rb.std(axis=0) / np.sqrt(len(rb) - 1)
    return mean, err


def make_avg_rectangle(h, mean, err):
    x0, x1 = plt.xlim()
    color = h[0].get_color()
    rect = plt.Rectangle([x0, mean - err], x1-x0, 2 * err, alpha=.9,
                             facecolor=color, edgecolor=None)
    plt.gca().add_patch(rect)

def plot_mc(method="VMC"):
    with h5py.File(method.lower()+"benzene.hdf5", "r") as hdf:
        energy = np.array(hdf["energytotal"])

    warmup = 20
    mean, err = rb_summary(energy, warmup, 40)

    #plt.figure(figsize=(4, 2))
    h = plt.plot(np.arange(len(energy)), energy, label=method.upper())
    rect = make_avg_rectangle(h, mean, err)
    #plt.gca().add_patch(rect)

    #plt.xlabel(method.upper() + " step")
    #plt.ylabel("E (Ha)")
    #plt.title(method.upper() + " energy")
    #plt.savefig("benzene_{0}.pdf".format(method.lower()), bbox_inches="tight")

def plot_both():
    energy = {}
    for method in ["vmc", "dmc"]:
        with h5py.File(method+"benzene.hdf5", "r") as hdf:
            energy[method] = np.array(hdf["energytotal"])

    plt.figure(figsize=(4, 3))
    h = {}
    for k, v in energy.items():
        h[k] = plt.plot(np.arange(len(v)), v, label=k.upper())
    for k, v in energy.items():
        warmup = 20
        mean, err = rb_summary(v, warmup, 40)
        make_avg_rectangle(h[k], mean, err)

    plt.xlabel("MC step")
    plt.ylabel("E (Ha)")
    plt.title("Energy trace")
    plt.legend()
    plt.savefig("benzene_both.pdf", bbox_inches="tight")

if __name__ == "__main__":
    plot_linemin()
    plot_both()
    plt.show()
