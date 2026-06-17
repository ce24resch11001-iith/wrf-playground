# WPS Geographical Static Data Setup

This section describes the download and installation of geographical static data required by `geogrid.exe` during the WRF preprocessing stage.

## Official Source

WPS Geographical Input Data:

https://www2.mmm.ucar.edu/wrf/users/download/get_sources_wps_geog.html

---

## Mandatory Static Data

Two mandatory geographical datasets are available:

### High Resolution Mandatory Dataset (Recommended)

- Highest resolution of each mandatory field
- Recommended for most applications
- ~2.6 GB compressed (~29 GB uncompressed)

Download:

```bash
wget https://www2.mmm.ucar.edu/wrf/src/wps_files/geog_high_res_mandatory.tar.gz
````

### Low Resolution Mandatory Dataset

* Lowest resolution mandatory fields
* Useful for testing and educational purposes

Download:

```bash
wget https://www2.mmm.ucar.edu/wrf/src/wps_files/geog_low_res_mandatory.tar.gz
```

---

## Installation

Move to the WPS geographical data directory:

```bash
cd /path/to/WPS_GEOG
```

Extract the downloaded dataset:

```bash
tar -xvzf geog_high_res_mandatory.tar.gz
```

or:

```bash
tar -xvzf geog_low_res_mandatory.tar.gz
```

After extraction, set the path in `namelist.wps`:

```fortran
&geogrid
 geog_data_path = '/path/to/WPS_GEOG'
/
```

---

## Verify Installation

Check that the geographical fields are available:

```bash
ls /path/to/WPS_GEOG
```

Expected directories include:

```
albedo_modis/
greenfrac_fpar_modis/
lai_modis_10m/
modis_landuse_20class_30s_with_lakes/
soiltype_bot_30s/
soiltype_top_30s/
topo_gmted2010_30s/
```

The WPS geographical data is now ready for running:

```bash
./geogrid.exe
```

---

## Notes

* The high-resolution mandatory dataset is recommended for research simulations.
* Additional application-specific static datasets can be added to the same `geog_data_path`.
* Keep the extracted geographical data directory unchanged after installation.

```
```
