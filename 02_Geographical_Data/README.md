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

# Directory Contents

```
02_Geographical_Data/
│
├── README.md
├── modis_cglc_lcz.md
├── frc_urb2d.md
├── common_errors.md
└── geogrid_tbl_examples.md
```

---

# Documentation Files

## 1. modis_cglc_lcz.md

Documentation for integrating **MODIS Land Cover and Local Climate Zone (LCZ)** datasets into WRF.

Topics covered:

- Overview of MODIS LCZ datasets
- Importance of LCZ classification for urban modelling
- Downloading and installing LCZ data
- Placement inside the WPS geographical database
- Required directory structure
- `GEOGRID.TBL` configuration
- Running `geogrid.exe` with LCZ data

Applications:

- Urban climate simulations
- Urban heat island studies
- City-scale meteorological modelling
- Urban canopy parameterization studies

---

## 2. frc_urb2d.md

Documentation for the **FRC_URB2D (Urban Fraction)** geographical variable.

FRC_URB2D represents the fraction of urban area within each model grid cell and is an important input for urban parameterization schemes.

Topics covered:

- Purpose of urban fraction data
- Relationship with urban canopy models
- Integration with WRF urban physics schemes
- Data preparation requirements
- Validation and visualization methods

Applications:

- Urban Weather Research
- Urban Heat Island simulations
- High-resolution WRF modelling
- Urban land-surface representation

---

---

## 3. geogrid_tbl_examples.md

Documentation and examples for modifying the WPS `GEOGRID.TBL` file.

The `GEOGRID.TBL` controls how geographical datasets are read and processed by `geogrid.exe`.

Topics covered:

- Structure of `GEOGRID.TBL`
- Field definitions
- Dataset priority
- Interpolation methods
- Multiple dataset handling
- Custom geographical variable configuration

---

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
            |
            ↓
Install into WPS_GEOG
            |
            ↓
Modify GEOGRID.TBL if required
            |
            ↓
Run geogrid.exe
            |
            ↓
Check geo_em.d0*.nc output
            |
            ↓
Proceed to atmospheric preprocessing
```

---

# References

- WRF Users Guide
- WPS Geographical Data Documentation
- NCAR Mesoscale and Microscale Meteorology Laboratory Documentation
- MODIS Land Cover Documentation
- Local Climate Zone (LCZ) Classification Framework

---

# Author Notes

This section provides a structured guide for integrating geographical datasets into WRF simulations with emphasis on:

- Reproducible workflows
- Urban climate modelling
- High-resolution simulations
- Custom geographical dataset integration

The goal is to help researchers understand not only **how to install geographical data**, but also **why each dataset influences WRF simulations**.
