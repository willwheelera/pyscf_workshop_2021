from dask.distributed import Client
from dask_kubernetes import KubeCluster

# See example at https://kubernetes.dask.org/en/latest/kubecluster.html#kubecluster
cluster = KubeCluster.from_yaml('worker-spec.yml')
cluster.scale(10)  # specify number of workers explicitly
cluster.adapt(minimum=1, maximum=100)  # or dynamically scale based on current workload

with Client(cluster) as client:
    pyqmc.recipes.OPTIMIZE(chkfile, "h2o_opt2.chk", client=client, npartitions=2)
cluster.close()
