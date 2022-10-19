import matplotlib.pyplot as plt
import pandas as pd
import h5py
import numpy as np


def plot_linemin():
    fname = "opt.hdf5"
    with h5py.File(fname, "r") as hdf:
        energy = np.array(hdf["energy"])
        energy_error = np.array(hdf["energy_error"])

    plt.figure(figsize=(4, 2))
    plt.errorbar(range(len(energy)), energy, energy_error)
    plt.xlabel("optimization step")
    plt.ylabel("energy (Ha)")
    plt.title(r"H$_2$O wave function optimization")
    plt.savefig("h2o_linemin.pdf", bbox_inches="tight")


def rb_summary(energy, warmup, nblocks):
    import pyqmc
    rb = pyqmc.reblock.reblock(energy[warmup:], nblocks)
    mean = rb.mean(axis=0)
    err = rb.std(axis=0) / np.sqrt(len(rb) - 1)
    return mean, err


def make_avg_rectangle(h, mean, err):
    x0, x1 = plt.xlim()
    color = h[0].get_color()
    rect = plt.Rectangle([x0, mean - err], x1-x0, 2 * err, alpha=.3,
                             facecolor=color, edgecolor=None)
    plt.gca().add_patch(rect)

def plot_mc(method="VMC"):
    with h5py.File(method.lower()+".hdf5", "r") as hdf:
        energy = np.array(hdf["energytotal"])

    mean, err = rb_summary(energy, 20, 40)

    #plt.figure(figsize=(4, 2))
    h = plt.plot(np.arange(len(energy)), energy, label=method.upper())
    rect = make_avg_rectangle(h, mean, err)
    #plt.gca().add_patch(rect)

    #plt.xlabel(method.upper() + " step")
    #plt.ylabel("E (Ha)")
    #plt.title(method.upper() + " energy")
    #plt.savefig("h2o_{0}.pdf".format(method.lower()), bbox_inches="tight")

def plot_both():
    energy = {}
    for method in ["vmc", "dmc"]:
        with h5py.File(method+".hdf5", "r") as hdf:
            energy[method] = np.array(hdf["energytotal"])

    plt.figure(figsize=(4, 3))
    h = {}
    for k, v in energy.items():
        h[k] = plt.plot(np.arange(len(v)), v, label=k.upper())
    for k, v in energy.items():
        mean, err = rb_summary(v, 20, 40)
        make_avg_rectangle(h[k], mean, err)

    plt.xlabel("MC step")
    plt.ylabel("E (Ha)")
    plt.title("Energy trace")
    plt.legend()
    plt.savefig("h2o_both.pdf", bbox_inches="tight")

if __name__ == "__main__":
    plot_linemin()
    #plot_both()
    #plt.show()
