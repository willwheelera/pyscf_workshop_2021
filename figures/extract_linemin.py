import h5py
import numpy as np
import pandas as pd

fname = "redo_si_example.opt.hdf"
with h5py.File(fname, "r") as hdf:
    df = {k: np.array(hdf[k]) for k in ["energy", "energy_error"]}

pd.DataFrame(df).to_csv("linemindata.csv")
