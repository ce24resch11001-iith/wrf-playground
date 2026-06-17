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
├── static_geographic_data.md
├── modis_cglc_lcz.md
├── frc_urb2d.md
├── common_errors.md
└── geogrid_tbl_examples.md
```

---

## Documentation Files

### `static_geographic_data.md`

Documentation for downloading and installing WPS geographical datasets.

Topics covered:

* WPS geographical data overview
* Mandatory dataset downloads
* Dataset installation
* `geog_data_path` configuration
* Installation verification

---

### `modis_cglc_lcz.md`

Documentation for integrating MODIS CGLC-LCZ data into WRF.

Topics covered:

* LCZ dataset overview
* Installation and directory placement
* `GEOGRID.TBL` configuration
* Running `geogrid.exe` with LCZ data

Applications:

* Urban climate simulations
* Urban heat island studies
* Urban canopy modelling

---

### `frc_urb2d.md`

Documentation for the `FRC_URB2D` (urban fraction) geographical variable.

Topics covered:

* Urban fraction datasets
* Integration with urban parameterization schemes
* Data preparation
* Validation and visualization

Applications:

* Urban meteorology
* Urban land-surface representation
* High-resolution WRF simulations

---

### `geogrid_tbl_examples.md`

Documentation and examples for modifying `GEOGRID.TBL`.

Topics covered:

* File structure
* Dataset priority
* Interpolation methods
* Custom geographical variables

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

## Common Geographical Datasets

| Dataset             | Purpose                            |
| ------------------- | ---------------------------------- |
| MODIS Land Cover    | Land-use classification            |
| MODIS CGLC-LCZ      | Urban morphology classification    |
| FRC_URB2D           | Urban fraction                     |
| GMTED2010           | Terrain elevation                  |
| Soil Categories     | Soil properties                    |
| Vegetation Fraction | Surface vegetation characteristics |

---

## Resolution Considerations

| WRF Resolution | Recommended Dataset Type                    |
| -------------- | ------------------------------------------- |
| 27–9 km        | Default WPS geographical data               |
| 3–1 km         | High-resolution land-use and urban datasets |
| <1 km          | Local or custom datasets                    |

For urban simulations, higher-resolution geographical datasets are generally preferred.

---

## Dataset Priority

When multiple datasets provide the same geographical variable, dataset selection is controlled through `GEOGRID.TBL`.

Example:

```text
MODIS LCZ > MODIS Land Cover > USGS Land Use
```

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
Update GEOGRID.TBL (if required)
        ↓
Run geogrid.exe
        ↓
Verify geo_em.d0*.nc
        ↓
Proceed to ungrib.exe
```

---

## References

* WRF Users Guide
  https://www2.mmm.ucar.edu/wrf/users/wrf_users_guide/build/html/index.html

* WPS Geographical Data Downloads
  https://www2.mmm.ucar.edu/wrf/users/download/get_sources_wps_geog.html

* WRF Online Tutorial
  https://www2.mmm.ucar.edu/wrf/OnLineTutorial/compilation_tutorial.php

* MODIS CGLC-LCZ Technical Documentation
  https://doi.org/10.5281/zenodo.7670792
