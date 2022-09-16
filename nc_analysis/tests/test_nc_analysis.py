from nc_analysis import Dataset

def test_nc_analysis():
    # with pytest, filenames are relative to top directory
    filename = "./nc_analysis/sample_data/DBRD-NATURE2020-depth.r0.1.nc"
    ds = Dataset(filename)
    assert hasattr(ds, "ds")
    assert "dvs" in ds.ds.variables
