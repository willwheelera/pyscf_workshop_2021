from pyscf import gto, scf 
import ase.build 
from pyscf.pbc.tools.pyscf_ase import ase_atoms_to_pyscf

benzene = ase.build.molecule("C6H6")
mol = gto.M(
    atom=ase_atoms_to_pyscf(benzene),
    basis="ccecp-ccpvtz",
    ecp="ccecp",
)
mf = scf.RHF(mol)
mf.chkfile = "scf.chk"
mf.run()
