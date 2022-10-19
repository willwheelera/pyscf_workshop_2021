from concurrent.futures import ProcessPoolExecutor

with ProcessPoolExecutor() as client:
    pyqmc.OPTIMIZE(
        "scf.chk", "opt1.chk", 
        client=client, npartitions=2
    )
