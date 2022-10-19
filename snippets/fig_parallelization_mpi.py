from mpi4py.futures import MPIPoolExecutor
import mpi4py.MPI

if __name__ == "__main__":
    npartitions = mpi4py.MPI.COMM_WORLD.Get_size()-1
    with MPIPoolExecutor() as client:
        pyqmc.OPTIMIZE("scf.chk", "opt2.chk", client=client, npartitions=2)
