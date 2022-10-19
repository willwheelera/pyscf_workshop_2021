from pyscf.pbc import gto, scf
import numpy as np

cell = gto.Cell(
    atom="""Si 0.   0.   0. 
            Si 1.36 1.36 1.36""",
    a=np.array([[0, 1, 1],
                [1, 0, 1],
                [1, 1, 0]]) * 2.72,
    basis="ccecp-ccpvtz", ecp="ccecp",
)
cell.exp_to_discard = 0.1
cell.build()

kpts = cell.make_kpts([8, 8, 8])
mf = scf.KRKS(cell, kpts=kpts)
mf.chkfile = "scf.chk"
mf.run()
