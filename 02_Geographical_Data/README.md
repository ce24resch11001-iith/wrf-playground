# 02 - Geographical Data

## Overview

This directory contains documentation related to the geographical datasets used by the WRF modeling system.

These datasets describe the physical characteristics of the Earth's surface and are processed by `geogrid.exe` during WPS preprocessing to generate the `geo_em.d0*.nc` files required by WRF.

Geographical datasets influence:

* Terrain elevation
* Land use and land cover
* Soil properties
* Vegetation characteristics
* Urban morphology
* Surface parameters

---

## Role in the WRF Workflow

```text
Geographical Data
        ↓
    geogrid.exe
        ↓
  geo_em.d0*.nc
        ↓
    ungrib.exe
        ↓
    metgrid.exe
        ↓
     real.exe
        ↓
     wrf.exe
```

The generated `geo_em.d0*.nc` files contain static geographical information for every model grid cell.

---

## Directory Contents

```text
02_Geographical_Data/
│
├── README.md
├── 01_static_geographic_data.md
├── cglc_modis_lcz.md
├── frc_urb2d.md
├── GEOGRID.TBL.ARW_LCZ
└── common_errors.md
```

---

## Documentation Files

### `01_static_geographic_data.md` (mandatory)

Documentation for downloading and installing WPS geographical datasets.

Topics covered:

* WPS geographical data overview
* Dataset installation
* `geog_data_path` configuration
* Installation verification

---

### `cglc_modis_lcz.md` (optional)

Documentation for integrating CGLC MODIS LCZ data into WRF.

Topics covered:

* CGLC-MODIS-LCZ dataset overview and LCZ classification
* WRF-WPS integration through `GEOGRID.TBL` and `namelist.wps`
* Verification and visualization of LCZ land-use data

Applications: Enhanced representation of urban morphology for urban climate and urban heat island simulations in WRF.

---

### `frc_urb2d.md` (optional)

Documentation for the `FRC_URB2D` (urban fraction) geographical variable.

Topics covered:

* Global urban fraction dataset overview
* Integration into WRF-WPS through geogrid.exe
* Verification and visualization of `FRC_URB2D`

Applications: Urban meteorology, urban climate studies, and improved urban land-surface representation in WRF simulations.

---

### `GEOGRID.TBL.ARW_LCZ` (Example File)

Includes:

* Integrating `cglc_modis_lcz` dataset (`line 24-29` as `LANDUSEF`)
* Integrating `frc_urb2d` dataset (`line 438-445` as `FRC_URB2D`)

---

### `common_errors.md`

Common issues related to geographical datasets and `geogrid.exe`.

Topics covered:

* Missing geographical fields
* Incorrect `geog_data_path`
* `GEOGRID.TBL` configuration issues
* `geogrid.exe` failures

---

## WPS Geographical Data Structure

Example:

```text
WPS_GEOG/
│
├── albedo_modis/
├── greenfrac_fpar_modis/
├── modis_landuse_20class_30s_with_lakes/
├── topo_gmted2010_30s/
├── CGLC_MODIS_LCZ_global/
└── urbfrac_1km/
```

The geographical data location is specified in `namelist.wps`:

```fortran
&geogrid
 geog_data_path = '/path/to/WPS_GEOG'
/
```

---

## Common Geographical Variables and Datasets

The table below lists some commonly used geographical variables available in WRF geographical datasets and `geo_em.d0*.nc` files.

| WRF Variable | Description | Example Dataset |
|--------------|-------------|-----------------|
| `HGT_M` | Terrain elevation | GMTED2010 |
| `LU_INDEX` | Dominant land-use category | MODIS Land Cover |
| `LANDUSEF` | Fractional land-use coverage | MODIS Land Cover, CGLC MODIS-LCZ |
| `FRC_URB2D` | Urban fraction within a grid cell | Global Urban Fraction Dataset |
| `SOILTYP` | Soil category | WPS Soil Datasets |
| `GREENFRAC` | Monthly vegetation fraction | MODIS Green Fraction |
| `ALBEDO12M` | Monthly surface albedo | MODIS Albedo |
| `URB_PARAM`* | Urban canopy parameters | Urban parameter datasets |

\* Available when urban datasets and parameterizations are configured.

## Dataset Selection Considerations

The benefit of high-resolution geographical datasets generally increases as model resolution becomes finer. For urban and convection-permitting simulations (≤3 km), datasets such as LCZ and urban fraction products can improve surface representation compared to default WPS datasets.

When multiple datasets provide the same geographical variable, the dataset used by `geogrid.exe` is determined by the corresponding `GEOGRID.TBL` configuration.

---

## Verification

After running `geogrid.exe`, verify that the output files were generated successfully:

```bash
ncdump -h geo_em.d01.nc
```

Check:

* Required variables are present
* No missing geographical fields
* `geogrid.exe` completed without errors

---

## Recommended Workflow

```text
Download dataset
        ↓
Install into WPS_GEOG
        ↓
Update linked GEOGRID.TBL (if required)
        ↓
Run geogrid.exe
        ↓
Verify geo_em.d0*.nc
        ↓
Proceed to ungrib.exe
```

---

## References

* WRF Users Guide : https://www2.mmm.ucar.edu/wrf/users/wrf_users_guide/build/html/index.html

* WPS Geographical Data Downloads : https://www2.mmm.ucar.edu/wrf/users/download/get_sources_wps_geog.html

* WRF Online Tutorial : https://www2.mmm.ucar.edu/wrf/OnLineTutorial/compilation_tutorial.php

* MODIS CGLC-LCZ Technical Documentation : Matthias Demuzere, Cenlin He, Alberto Martilli, & Andrea Zonato. (2023). Technical documentation for the hybrid 100-m global land cover dataset with Local Climate Zones for WRF (1.0.0). Zenodo. https://doi.org/10.5281/zenodo.7670792

* Global Urban Fraction Dataset : Patel, P., & Roth, M. (2022). A High-Resolution Dataset of Global Urban Fraction for Mesoscale Urban Modelling (2.0.1) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.7298393
