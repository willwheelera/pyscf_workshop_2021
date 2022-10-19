import pyscf.tools
import matplotlib.pyplot as plt

mol, mf = pyqmc.recover_pyscf("h2o.hdf5")
ao_rdm1 = np.einsum("pi,ij,qj->pq", mf.mo_coeff, rdm1, mf.mo_coeff.conj())
dens = pyscf.tools.cubegen.density(
    mol, "h2o_sj_density.cube", ao_rdm1, resolution=0.05
)

xcenter = int(dens.shape[0]/2)
plt.contourf(
    dens[xcenter], 
    levels=np.max(dens[xcenter]) * np.logspace(-6, -1, 80),
)
