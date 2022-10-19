S = 2 * np.eye(3) # 2x2x2 supercell
S = [[-1,  1,  1], 
     [ 1, -1,  1], 
     [ 1,  1, -1]] # conventional cell
pyqmc.OPTIMIZE(
    "si_scf.chk", "si_opt.chk", S=S
)
