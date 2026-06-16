# MODIS CGLC-LCZ: Hybrid 100-m Global Land Cover Dataset with Local Climate Zones for WRF

## Overview

The **CGLC-MODIS-LCZ (Copernicus Global Land Cover - MODIS - Local Climate Zone)** dataset is a high-resolution geographical dataset developed for the **Weather Research and Forecasting (WRF)** model.

It combines:

1. **Copernicus Global Land Service Land Cover (CGLC)** converted to MODIS IGBP land-use classes.
2. **Local Climate Zone (LCZ)** classification representing urban morphology.

The dataset improves representation of surface heterogeneity, particularly for urban simulations involving:

- Urban climate
- Urban heat islands
- Air quality modelling
- Urban canopy parameterization

---

# Attribution

The original dataset was developed by:

**Demuzere, M., He, C., Martilli, A., & Zonato, A. (2023)**

*A hybrid 100-m global land cover dataset with Local Climate Zones for WRF.*

Dataset:

```
https://doi.org/10.5281/zenodo.7670653
```

Technical documentation:

```
https://doi.org/10.5281/zenodo.7670792
```

This document describes the WRF/WPS implementation workflow and does not redistribute or modify the original dataset.

---

# Dataset Information

| Parameter | Description |
|-----------|-------------|
| Dataset | Hybrid 100-m Global Land Cover Dataset with LCZ for WRF |
| Version | 1.0.0 |
| Resolution | 100 m |
| Reference year | 2018 |
| Coverage | 180°W–180°E, 60°S–78°N |

## Dataset Developers

- Matthias Demuzere
- Cenlin He
- Alberto Martilli
- Andrea Zonato

---

# Dataset Components

## 1. CGLC-MODIS Land Cover

The CGLC product is converted into MODIS IGBP-compatible land-use classes.

It represents:

- Forest
- Shrublands
- Grasslands
- Croplands
- Wetlands
- Water
- Urban areas
- Barren regions

---

## 2. Local Climate Zones (LCZ)

LCZ describes urban morphology using characteristics such as:

- Building density
- Building height
- Surface cover
- Urban structure
- Thermal properties

LCZ categories allow WRF to represent different urban environments instead of a single urban class.

---

# CGLC-MODIS-LCZ Land Categories in WRF

The WRF implementation uses:

```
MODIS IGBP classes : 1 - 21

LCZ classes        : 51 - 61
```

The LCZ numbering avoids conflicts with existing WRF land-use categories.

---

# MODIS IGBP Land Cover Categories

| ID | Class |
|----|-------|
| 1 | Evergreen Needleleaf Forest |
| 2 | Evergreen Broadleaf Forest |
| 3 | Deciduous Needleleaf Forest |
| 4 | Deciduous Broadleaf Forest |
| 5 | Mixed Forests |
| 6 | Closed Shrublands |
| 7 | Open Shrublands |
| 8 | Woody Savanna |
| 9 | Savanna |
| 10 | Grasslands |
| 11 | Permanent Wetlands |
| 12 | Croplands |
| 13 | Urban and Built-up Land |
| 14 | Cropland/Natural Vegetation Mosaic |
| 15 | Snow and Ice |
| 16 | Barren or Sparsely Vegetated |
| 17 | Water |
| 18 | Wooded Tundra |
| 19 | Mixed Tundra |
| 20 | Barren Tundra |
| 21 | Lake |

---

# LCZ Categories in WRF

| WRF ID | LCZ | Description |
|--------|-----|-------------|
| 51 | LCZ 1 | Compact High-Rise |
| 52 | LCZ 2 | Compact Mid-Rise |
| 53 | LCZ 3 | Compact Low-Rise |
| 54 | LCZ 4 | Open High-Rise |
| 55 | LCZ 5 | Open Mid-Rise |
| 56 | LCZ 6 | Open Low-Rise |
| 57 | LCZ 7 | Lightweight Low-Rise |
| 58 | LCZ 8 | Large Low-Rise |
| 59 | LCZ 9 | Sparsely Built |
| 60 | LCZ 10 | Heavy Industry |
| 61 | LCZ E | Bare Rock or Paved |

---

# WRF/WPS Implementation

Supported from:

```
WRF/WPS version 4.5+
```

The dataset is implemented through:

- Tiled binary geographical files
- Index files
- GEOGRID.TBL configuration

Processing is performed during:

```
geogrid.exe
```

---

# Dataset Download

Source:

```
https://www2.mmm.ucar.edu/wrf/src/wps_files/cglc_modis_lcz_global.tar.gz
```

Extract into:

```
WPS_GEOG/

└── CGLC_MODIS_LCZ_global/
```

---

# GEOGRID.TBL Configuration

File:

```
WPS/geogrid/GEOGRID.TBL.ARW_LCZ
```

Entry:

```text
name=LANDUSEF
        priority = 2
        dest_type = categorical
        z_dim_name = land_cat
        interp_option = cglc_modis_lcz:nearest_neighbor
        rel_path = cglc_modis_lcz:CGLC_MODIS_LCZ_global/
```

---

# namelist.wps Configuration

```fortran
&geogrid
 geog_data_res = 'cglc_modis_lcz+default'
/
```

`+default` allows WPS to use default geographical datasets where CGLC-MODIS-LCZ coverage is unavailable.

---

# Processing Workflow

```
CGLC-MODIS-LCZ Download
          |
          ↓
Extract into WPS_GEOG
          |
          ↓
Configure GEOGRID.TBL
          |
          ↓
Update namelist.wps
          |
          ↓
Run geogrid.exe
          |
          ↓
Generate geo_em.d0*.nc
```

---

# Visualization Examples

CGLC-MODIS-LCZ maps generated for Indian cities:

```
Resolution: 1 km
```

Examples:

- Hyderabad
- Delhi
- Mumbai
- Kolkata

Images:

```
images/hyderabad_cglc_lcz_1km.png
images/delhi_cglc_lcz_1km.png
images/mumbai_cglc_lcz_1km.png
images/kolkata_cglc_lcz_1km.png
```

---

# Verification

After running:

```bash
geogrid.exe
```

Check:

```
geo_em.d01.nc
```

Variables:

```
LANDUSEF
LANDUSE
```

Example:

```bash
ncdump -h geo_em.d01.nc | grep LANDUSE
```

---

# References

1. Buchhorn, M., et al. (2021).  
Copernicus Global Land Service Land Cover 100m.

2. Demuzere, M., et al. (2022).  
A global map of local climate zones to support earth system modelling and urban-scale environmental science.  
Earth System Science Data, 14, 3835–3873.

3. Demuzere, M., He, C., Martilli, A., & Zonato, A. (2023).  
A hybrid 100-m global land cover dataset with Local Climate Zones for WRF.

---

# Notes

CGLC-MODIS-LCZ provides improved urban surface representation for WRF simulations by combining detailed land-cover information with LCZ-based urban classification.

This workflow is particularly useful for high-resolution urban simulations over cities such as Hyderabad, Delhi, Mumbai, and Kolkata.
