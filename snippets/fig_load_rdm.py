def avg(vec):
    avg = np.mean(vec, axis=0)
    err = sem(vec, axis=0)
    return avg, err


with h5py.File("h2o_vmc.hdf5") as f:
    warmup = 2
    rdm1, rdm1_err = avg(f["rdm1value"][warmup:, ...])
    rdm1norm, rdm1norm_err = avg(f["rdm1norm"][warmup:, ...])
    rdm1 = pyqmc.obdm.normalize_obdm(rdm1, rdm1norm)
    rdm1_err = pyqmc.obdm.normalize_obdm(rdm1_err, rdm1norm)
