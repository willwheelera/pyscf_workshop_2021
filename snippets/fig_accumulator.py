import numpy as np


class DipoleAccumulator:
  def __init__(self):
    pass

  def __call__(self, configs, wf):
    dipole = configs.configs.sum(axis=1)
    return {"electric_dipole": dipole}

  def avg(self, configs, wf):
    d = {}
    for k, it in self(configs, wf).items():
      d[k] = np.mean(it, axis=0)
    return d

  def shapes(self):
    return {"electric_dipole": (3,)}

  def keys(self):
    return self.shapes().keys()


accumulators = dict(extra_accumulators={"dipole": DipoleAccumulator())
pyqmc.VMC(
    "scf.chk", 
    "dipole.hdf5", 
    start_from="opt.hdf5", 
    accumulators=accumulators,
)
