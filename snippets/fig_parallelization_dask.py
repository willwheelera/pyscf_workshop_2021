from dask.distributed import Client, LocalCluster

if __name__ == "__main__":
  n_workers = 2
  with LocalCluster(n_workers=n_workers) as cluster:
    with Client(cluster) as client:
      pyqmc.OPTIMIZE(
        "scf.chk", "opt3.chk", client=client, npartitions=n_workers
      )
