from sklearn.cluster import KMeans
import numpy as np

def calc_kmeans(x1, x2, n_clusters):
    """ a wrapper to call sklearn.cluster.Kmeans

    Parameters
    ----------
    x1 : array_like
        first variable to cluster
    x2 : array_like
        second variable to cluster
    n_clusters: int
        how many clusters to use in kmeans calculation

    Returns
    -------
    a fitted sklearn KMeans model
    """
    Xcluster = np.column_stack((x1, x2))
    clustering = KMeans(n_clusters=n_clusters).fit(Xcluster)
    return clustering
