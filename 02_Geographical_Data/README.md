# 02 - Geographical Data

## Overview

This directory contains documentation and resources related to **static geographical datasets** required for running the WRF (Weather Research and Forecasting) model.

Unlike atmospheric forcing datasets, geographical datasets represent the **physical characteristics of the Earth's surface**. These datasets are used during the **geogrid.exe** stage of the WRF Preprocessing System (WPS) to create geographical input files (`geo_em.d0*.nc`) required for model initialization.

Geographical datasets control how WRF represents:

- Terrain elevation
- Land use and land cover
- Soil characteristics
- Vegetation properties
- Urban morphology
- Surface parameters
- Land-surface processes

---

# Role in WRF Workflow

Geographical datasets are processed during the first stage of the WRF preprocessing workflow:

```
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

The generated `geo_em.d0*.nc` files contain static information for every WRF grid cell and are used by the model throughout the simulation.

---

```markdown
# Directory Contents

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

# Documentation Files

## 1. `static_geographic_data.md`

Documentation for downloading and installing WPS geographical static datasets.

Topics covered:

- WPS geographical data overview
- Mandatory static dataset downloads
- Dataset installation and directory structure
- Configuring `geog_data_path` in `namelist.wps`
- Verification of geographical data installation

---

## 2. `modis_cglc_lcz.md`

Documentation for integrating **MODIS CGLC-LCZ (Local Climate Zone)** data into WRF.

Topics covered:

- LCZ dataset overview
- Installation and directory placement
- `GEOGRID.TBL` configuration
- Running `geogrid.exe` with LCZ data

Applications:

- Urban climate simulations
- Urban heat island studies
- Urban canopy modelling

---

## 3. `frc_urb2d.md`

Documentation for the **FRC_URB2D (Urban Fraction)** geographical variable.

Topics covered:

- Purpose of urban fraction data
- Integration with WRF urban parameterization schemes
- Data preparation requirements
- Validation and visualization

Applications:

- Urban meteorological simulations
- Urban land-surface representation
- High-resolution WRF modelling

---

## 4. `geogrid_tbl_examples.md`

Documentation and examples for modifying the WPS `GEOGRID.TBL` configuration.

Topics covered:

- `GEOGRID.TBL` structure
- Geographical variable definitions
- Dataset priority and selection
- Interpolation methods
- Custom geographical field configuration

---

## 5. `common_errors.md`

Documentation for common issues related to WPS geographical data.

Topics covered:

- Missing geographical fields
- Incorrect `geog_data_path`
- `GEOGRID.TBL` configuration errors
- `geogrid.exe` failures
```


# WPS Geographical Data Structure

A typical WPS geographical dataset directory:

```
WPS_GEOG/
│
├── topography/
│
├── landuse/
│
├── soiltype/
│
├── vegetation/
│
├── modis_cglc_lcz/
│
└── frc_urb2d/
```

The location of geographical datasets is specified in:

```
namelist.wps
```

Example:

```fortran
&geogrid
 geog_data_path = '/path/to/WPS_GEOG'
/
```

---

# Common Geographical Datasets Used in WRF

| Dataset | Description | WPS Stage |
|---------|-------------|-----------|
| USGS Land Use | Traditional land-use classification | geogrid.exe |
| MODIS Land Cover | Updated satellite-based land classification | geogrid.exe |
| MODIS CGLC LCZ | Urban morphology classification | geogrid.exe |
| FRC_URB2D | Urban land fraction | geogrid.exe |
| GMTED / ASTER | Terrain elevation | geogrid.exe |
| Soil Categories | Soil properties | geogrid.exe |
| Vegetation Fraction | Surface vegetation characteristics | geogrid.exe |

---

# Resolution Considerations

The choice of geographical dataset depends on the horizontal resolution of the WRF simulation.

| WRF Resolution | Recommended Geographical Data |
|----------------|------------------------------|
| 27 km - 9 km | Default WRF geographical datasets |
| 3 km - 1 km | High-resolution land-use and urban datasets |
| <1 km | Local/custom geographical datasets |

For urban simulations, higher-resolution datasets are preferred because urban characteristics vary significantly over short distances.

---

# Dataset Priority

When multiple datasets represent the same geographical variable, WRF uses the priority defined in:

```
GEOGRID.TBL
```

Higher-resolution and more detailed datasets should generally have higher priority.

Example:

```
MODIS LCZ > MODIS Land Cover > USGS Land Use
```

The priority determines which dataset is used when generating the final `geo_em.d0*.nc` files (based on its availabilty).

---

# Verification and Quality Checks

Before running WRF, verify that:

- Geographical datasets are correctly installed
- `geog_data_path` points to the correct directory
- Required entries exist in linked `GEOGRID.TBL`
- `geogrid.exe` completes without errors
- Output files contain expected variables

Example:

```bash
ncdump -h geo_em.d01.nc
```

To visualize grids:

```bash
ncl util/plotgrids_new.ncl
```

---

# Recommended Workflow

```
Download geographical dataset
            ↓
Install into WPS_GEOG
            ↓
Modify GEOGRID.TBL if required
            ↓
Run geogrid.exe
            ↓
Check geo_em.d0*.nc output
            ↓
Proceed to ungrib
```

---

# References

- WRF Users Guide - https://www2.mmm.ucar.edu/wrf/users/wrf_users_guide/build/html/index.html
- WPS Static Geographical Data Page - https://www2.mmm.ucar.edu/wrf/users/download/get_sources_wps_geog.html
- UCAR Mesoscale and Microscale Meteorology Laboratory Documentation - https://www2.mmm.ucar.edu/wrf/OnLineTutorial/compilation_tutorial.php
- MODIS CGLC Local Climate Zone (LCZ) Technical Documentation - Matthias Demuzere, Cenlin He, Alberto Martilli, & Andrea Zonato. (2023). Technical documentation for the hybrid 100-m global land cover dataset with Local Climate Zones for WRF (1.0.0). Zenodo. https://doi.org/10.5281/zenodo.7670792

---

# Author Notes

This section provides a structured guide for integrating geographical datasets into WRF simulations with emphasis on:

- Reproducible workflows
- Urban climate modelling
- High-resolution simulations
- Custom geographical dataset integration

The goal is to help researchers understand not only **how to install geographical data**, but also **why each dataset influences WRF simulations**.
