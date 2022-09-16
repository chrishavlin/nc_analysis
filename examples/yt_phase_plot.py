import yt
import netCDF4

filename = "../nc_analysis/sample_data/DBRD-NATURE2020-depth.r0.1.nc"

vars = ["lQ", "dvs", "mp"]
data = {}
with netCDF4.Dataset(filename) as nc_ds:
    for var in vars:
        data[var] = (nc_ds.variables[var][:].copy(), "")

domain_dims = data[vars[0]][0].shape
ds = yt.load_uniform_grid(data, domain_dims)

pp = yt.PhasePlot(ds.all_data(), ("stream", "dvs"), ("stream", "lQ"), ("stream", "mp"), weight_field=None)
pp.set_log(("stream", "dvs"), False)
pp.set_log(("stream", "lQ"), False)
pp.save()



