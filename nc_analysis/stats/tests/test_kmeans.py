from nc_analysis.stats import kmeans
import numpy as np


def test_kmeans():
    # just check that it runs
    z = np.linspace(0, 1, 50)

    x1 = np.exp((z - 0.25)**2/0.2)
    x2 = np.exp((z - 0.4)**2/0.2)

    _ = kmeans.calc_kmeans(x1, x2, 2)
