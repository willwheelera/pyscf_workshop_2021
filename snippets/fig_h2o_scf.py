from pyscf import gto, scf

mol = gto.M(
    atom="""
        O  0.000, 0.000, 0.0
        H  0.762, 0.479, 0.0
        H -0.762, 0.479, 0.0
    """,
    basis="ccecp-ccpvtz", 
    ecp="ccecp",
)
mf = scf.RHF(mol)
mf.chkfile = "scf.chk"
mf.run()
