# MODIS CGLC-LCZ: Hybrid 100-m Global Land Cover Dataset with Local Climate Zones for WRF

## Overview

The **CGLC-MODIS-LCZ (Copernicus Global Land Cover - MODIS - Local Climate Zone)** dataset is a high-resolution geographical dataset developed for use with the **Weather Research and Forecasting (WRF)** model.

This dataset improves the representation of land-surface characteristics by combining:

1. **Copernicus Global Land Service Land Cover (CGLC)** information converted to the MODIS IGBP land-use classification system.
2. **Global Local Climate Zone (LCZ)** information describing urban morphology and built environments.

The integration of land-cover information with urban classification provides a more realistic representation of surface heterogeneity, especially for simulations involving urban regions.

This dataset is particularly useful for:

- Urban meteorological simulations
- Urban heat island studies
- High-resolution WRF applications
- Urban canopy modelling
- City-scale air quality modelling
- Land-surface interaction studies

---

# Attribution

This documentation provides a practical guide for integrating the CGLC-MODIS-LCZ dataset into the WRF/WPS workflow.

The original dataset and scientific methodology were developed by:

**Demuzere, M., He, C., Martilli, A., & Zonato, A. (2023)**

*A hybrid 100-m global land cover dataset with Local Climate Zones for WRF.*

Dataset DOI:

```
https://doi.org/10.5281/zenodo.7670653
```

Technical documentation:

```
https://doi.org/10.5281/zenodo.7670792
```

This repository does not redistribute or modify the original dataset. It documents the installation, configuration, and usage workflow within WRF/WPS.

---

# Dataset Information

## Dataset Name

**A hybrid 100-m global land cover dataset with Local Climate Zones for WRF**

## Dataset Version

```
Version 1.0.0
```

## Dataset Developers

- Matthias Demuzere
- Cenlin He
- Alberto Martilli
- Andrea Zonato

## Representative Year

```
2018
```

## Spatial Resolution

```
100 m
```

## Geographic Coverage

```
Longitude:
-180°W to 180°E

Latitude:
-60°S to 78°N
```

---

# Dataset Components

## 1. CGLC-MODIS Land Cover

The Copernicus Global Land Cover dataset provides detailed information about surface categories.

For WRF implementation, the dataset is converted into MODIS IGBP-compatible land-use classes.

It represents categories such as:

- Forest regions
- Grasslands
- Croplands
- Wetlands
- Water surfaces
- Barren regions
- Urban and built-up areas

This provides improved surface characterization compared with older coarse-resolution land-use datasets.

---

## 2. Local Climate Zones (LCZ)

The Local Climate Zone framework classifies urban and natural landscapes based on their physical characteristics.

Important characteristics include:

- Building density
- Building height
- Surface cover
- Urban structure
- Thermal properties

LCZ information is especially valuable for urban modelling because cities contain highly heterogeneous surfaces that cannot be represented by a single urban land-use category.

---

# LCZ Classification Used in WRF

## Built Environment Classes

| LCZ | Description |
|----|-------------|
| LCZ 1 | Compact high-rise |
| LCZ 2 | Compact mid-rise |
| LCZ 3 | Compact low-rise |
| LCZ 4 | Open high-rise |
| LCZ 5 | Open mid-rise |
| LCZ 6 | Open low-rise |
| LCZ 7 | Lightweight low-rise |
| LCZ 8 | Large low-rise |
| LCZ 9 | Sparsely built |
| LCZ 10 | Heavy industry |

## Natural Environment Classes

| LCZ | Description |
|----|-------------|
| LCZ A | Dense trees |
| LCZ B | Scattered trees |
| LCZ C | Bush and scrub |
| LCZ D | Low plants |
| LCZ E | Bare rock |
| LCZ F | Bare soil |
| LCZ G | Water |

---

# Importance for WRF Urban Modelling

Traditional WRF simulations commonly use land-use datasets such as:

- USGS 24-category land-use data
- MODIS land-cover datasets

However, urban regions contain complex variations in:

- Building density
- Surface materials
- Urban geometry
- Vegetation distribution

The CGLC-MODIS-LCZ dataset improves urban representation by providing:

- Higher spatial resolution
- Detailed urban classification
- LCZ-based urban information
- Better land-surface heterogeneity

This is important for simulations involving:

- Megacities
- Urban heat islands
- Extreme temperature events
- Urban air pollution
- Surface energy exchange

---

# WRF/WPS Implementation

## WRF Compatibility

The dataset capability is officially available in:

```
WRF/WPS version 4.5+
```

The dataset is integrated into WPS as:

- Tiled binary geographical files
- Dataset index files
- GEOGRID table configuration

The data are processed during:

```
geogrid.exe
```

---

# Dataset Download

The dataset used in this workflow was obtained from:

```
https://www2.mmm.ucar.edu/wrf/src/wps_files/cglc_modis_lcz_global.tar.gz
```

After extraction:

```
WPS_GEOG/

└── CGLC_MODIS_LCZ_global/
    |
    ├── index
    ├── tiled binary files
    └── metadata files
```

---

# GEOGRID.TBL Configuration

The CGLC-MODIS-LCZ dataset requires an additional GEOGRID table definition.

File:

```
WPS/geogrid/GEOGRID.TBL.ARW_LCZ
```

Configuration:

```text
name=LANDUSEF
        priority = 2
        dest_type = categorical
        z_dim_name = land_cat
        interp_option = cglc_modis_lcz:nearest_neighbor
        rel_path = cglc_modis_lcz:CGLC_MODIS_LCZ_global/
```

## Parameter Description

| Parameter | Description |
|-----------|-------------|
| name | WRF geographical variable |
| priority | Dataset priority during processing |
| dest_type | Categorical dataset |
| z_dim_name | Land-use category dimension |
| interp_option | Nearest-neighbour interpolation |
| rel_path | Dataset location inside WPS_GEOG |

---

# namelist.wps Configuration

To activate CGLC-MODIS-LCZ:

```fortran
&geogrid
 geog_data_res = 'cglc_modis_lcz+default'
/
```

The `+default` option allows WPS to use standard geographical datasets for regions where CGLC-MODIS-LCZ does not provide coverage.

Examples:

- Ocean regions
- Polar regions
- Areas outside dataset limits

---

# WPS Processing Workflow

```
Download CGLC-MODIS-LCZ
            |
            ↓
Extract into WPS_GEOG
            |
            ↓
Configure GEOGRID.TBL
            |
            ↓
Modify namelist.wps
            |
            ↓
Run geogrid.exe
            |
            ↓
Generate geo_em.d0*.nc
            |
            ↓
Continue WRF preprocessing
```

---

# Visualization Examples

The following examples show CGLC-MODIS-LCZ representation over major Indian cities.

Generated visualizations:

```
Hyderabad
Delhi
Mumbai
Kolkata
```

Resolution:

```
1 km visualization scale
```

These maps demonstrate differences in urban morphology and land-cover characteristics between Indian metropolitan regions.

---

## Hyderabad

Insert:

```
images/hyderabad_cglc_lcz_1km.png
```

---

## Delhi

Insert:

```
images/delhi_cglc_lcz_1km.png
```

---

## Mumbai

Insert:

```
images/mumbai_cglc_lcz_1km.png
```

---

## Kolkata

Insert:

```
images/kolkata_cglc_lcz_1km.png
```

---

# Example Application: Indian Urban WRF Simulations

For city-scale simulations:

```
d01 : Regional scale
d02 : State scale
d03 : City scale
d04 : Urban neighbourhood scale
```

CGLC-MODIS-LCZ improves representation of:

- Urban expansion
- Built-up fraction
- Urban morphology
- Surface energy exchange
- Urban-atmosphere interactions

---

# Verification After geogrid.exe

After running:

```
geogrid.exe
```

check:

```
geo_em.d01.nc
```

Important variables:

```
LANDUSEF
LANDUSE
```

Example:

```bash
ncdump -h geo_em.d01.nc | grep LANDUSE
```

Visualization tools:

- QGIS
- Python xarray
- NCL utilities

---

# Technical Documentation

Official documentation:

```
Demuzere et al. (2023)

Technical documentation for the hybrid 100-m global land cover dataset with Local Climate Zones for WRF

DOI:
https://doi.org/10.5281/zenodo.7670792
```

Dataset:

```
Demuzere et al. (2023)

A hybrid 100-m global land cover dataset with Local Climate Zones for WRF

DOI:
https://doi.org/10.5281/zenodo.7670653
```

---

# References

1. Buchhorn, M., Smets, B., Bertels, L., et al. (2021).

Copernicus Global Land Service Land Cover 100m.


2. Demuzere, M., Kittner, J., Martilli, A., et al. (2022).

A global map of local climate zones to support earth system modelling and urban-scale environmental science.

Earth System Science Data, 14, 3835–3873.


3. Demuzere, M., He, C., Martilli, A., & Zonato, A. (2023).

A hybrid 100-m global land cover dataset with Local Climate Zones for WRF.

---

# Notes

The CGLC-MODIS-LCZ dataset provides an advanced geographical representation for WRF simulations by combining detailed land-cover information with urban morphology classification.

For Indian urban applications such as Hyderabad, Delhi, Mumbai, and Kolkata, this dataset enables improved representation of urban surfaces compared with traditional land-use datasets.

The implementation documented here focuses on reproducible WRF/WPS usage rather than reproducing the original dataset development methodology.
