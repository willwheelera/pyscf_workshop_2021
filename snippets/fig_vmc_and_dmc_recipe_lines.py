pyqmc.VMC(
    "scf.chk", 
    "vmc.hdf5", 
    start_from="opt.hdf5",
)

pyqmc.DMC(
    "scf.chk", 
    "dmc.hdf5", 
    start_from="opt.hdf5",
)
