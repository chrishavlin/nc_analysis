import netCDF4


def load_netcdf(filename):
    """ load a netcdf file

    Parameters
    ----------
    filename: str or PosixPath
        the file to load
    """
    return netCDF4.Dataset(filename)
