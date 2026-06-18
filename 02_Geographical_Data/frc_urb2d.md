# FRC_URB2D: Global Urban Fraction Dataset for WRF

## Overview

**FRC_URB2D** represents the fraction of a WRF grid cell covered by urban or impervious surfaces.

The dataset is derived from the **ESA WorldCover** land-cover product and provides global urban fraction fields in WRF-WPS format at resolutions ranging from 1° to 100 m.

FRC_URB2D is commonly used by urban canopy parameterization schemes to improve the representation of urban land surfaces and urban-atmosphere interactions.

Applications include:

- Urban and mesoscale atmospheric modelling
- High-resolution WRF simulations

---

## Attribution

The original dataset was developed by:

**Pratiman Patel & Matthias Roth (2022)**

*A High-Resolution Dataset of Global Urban Fraction for Mesoscale Urban Modelling.*

Dataset:

```text
https://doi.org/10.5281/zenodo.7298393
```

> **Note:** This document describes the WRF/WPS implementation workflow and does not redistribute or modify the original dataset.

---

## Dataset Information

| Parameter | Description                   |
| --------- | ----------------------------- |
| Dataset   | Global Urban Fraction Dataset |
| Version   | 2.0.1                         |
| Base Data | ESA WorldCover 2021 v200      |
| Coverage  | Global                        |
| Format    | GeoTIFF and WRF-WPS           |

## Dataset Developers

* Pratiman Patel
* Matthias Roth

---

## Available Resolutions

| Resolution | Approximate Scale |
| ---------- | ----------------- |
| 1°         | ~111 km           |
| 0.5°       | ~55 km            |
| 0.25°      | ~28 km            |
| 0.009°     | ~1 km             |
| 0.0027°    | ~300 m            |
| 0.0009°    | ~100 m            |

---

## WRF/WPS Implementation

The dataset is incorporated during:

```text
geogrid.exe
```

and becomes available in:

```text
geo_em.d0*.nc
```

through the variable:

```text
FRC_URB2D
```

The urban fraction values range from:

```text
0.0 → No urban coverage
1.0 → Fully urbanized grid cell
```

---

## Prerequisites

The urban fraction datasets are distributed as `.tar.bz2` archives.

Ensure that a bzip2 extractor is available on your system before downloading and extracting the files.

Ubuntu/Debian:

```bash
sudo apt update
sudo apt install -y bzip2
```

Verify installation:

```bash
which bzip2
```

Example extraction command (after downloading a dataset):

```bash
tar -xjvf urb_fraction_1km.tar.bz2
```
---

## Dataset Download

Download the required dataset directly into:

```text
WPS_GEOG/
```

## 1° Resolution

```bash
cd WPS_GEOG

wget -O urb_fraction_1d.tar.bz2 \
"https://zenodo.org/records/7298393/files/urb_fraction_1d.tar.bz2?download=1"

tar -xjvf urb_fraction_1d.tar.bz2
```

## 0.5° Resolution

```bash
cd WPS_GEOG

wget -O urb_fraction_0p50d.tar.bz2 \
"https://zenodo.org/records/7298393/files/urb_fraction_0p50d.tar.bz2?download=1"

tar -xjvf urb_fraction_0p50d.tar.bz2
```

## 0.25° Resolution

```bash
cd WPS_GEOG

wget -O urb_fraction_0p25d.tar.bz2 \
"https://zenodo.org/records/7298393/files/urb_fraction_0p25d.tar.bz2?download=1"

tar -xjvf urb_fraction_0p25d.tar.bz2
```

## 1 km Resolution

```bash
cd WPS_GEOG

wget -O urb_fraction_1km.tar.bz2 \
"https://zenodo.org/records/7298393/files/urb_fraction_1km.tar.bz2?download=1"

tar -xjvf urb_fraction_1km.tar.bz2
```

## 300 m Resolution

```bash
cd WPS_GEOG

wget -O urb_fraction_300m.tar.bz2 \
"https://zenodo.org/records/7298393/files/urb_fraction_300m.tar.bz2?download=1"

tar -xjvf urb_fraction_300m.tar.bz2
```

## 100 m Resolution

```bash
cd WPS_GEOG

wget -O urb_fraction_100m.tar.bz2 \
"https://zenodo.org/records/7298393/files/urb_fraction_100m.tar.bz2?download=1"

tar -xjvf urb_fraction_100m.tar.bz2
```

Extracted directories:

```text
urb_fraction_1d/
urb_fraction_0p50d/
urb_fraction_0p25d/
urb_fraction_1km/
urb_fraction_300m/
urb_fraction_100m/
```

---

## GEOGRID.TBL Configuration

Add the following entry to linked `GEOGRID.TBL` (see `GEOGRID.TBL.ARW_LCZ` `(line 438-445)` for example):

```text
name=FRC_URB2D
        priority=1
        optional=yes
        dest_type=continuous
        fill_missing=0.
        interp_option=default:average_gcell(2.0)+four_pt
        rel_path=default:urb_fraction_1km/
        flag_in_output=FLAG_FRC_URB2D
```

Replace:

```text
urb_fraction_1km
```

with the selected dataset resolution.

Examples:

```text
rel_path=default:urb_fraction_0p25d/
rel_path=default:urb_fraction_300m/
rel_path=default:urb_fraction_100m/
```

---

## Processing Workflow

```text
Urban Fraction Dataset Download
        ↓
Extract into WPS_GEOG
        ↓
Configure GEOGRID.TBL
        ↓
Run geogrid.exe
        ↓
Generate geo_em.d0*.nc
        ↓
Verify FRC_URB2D
```

---

## Visualization Examples

FRC_URB2D maps generated for Indian cities:

```text
Resolution: 1 km
```

Example Images:

```text
- Hyderabad : images/hyderabad_frc_urb2d_1km.png
- Delhi     : images/delhi_frc_urb2d_1km.png
- Mumbai    : images/mumbai_frc_urb2d_1km.png
- Kolkata   : images/kolkata_frc_urb2d_1km.png
```

---

## Verification

After running:

```bash
geogrid.exe
```

Check:

```text
geo_em.d01.nc
```

Important variable:

```text
FRC_URB2D
```

Verify that the variable exists:

```bash
ncdump -h geo_em.d01.nc | grep FRC_URB2D
```

Visualize using:

```bash
ncview geo_em.d01.nc
```

Select:

```text
FRC_URB2D
```

to inspect the spatial distribution of urban fraction values across the model domain.

Higher values indicate greater urban coverage within a grid cell.

---

## References

1. Patel, P., & Roth, M. (2022).
   *A High-Resolution Dataset of Global Urban Fraction for Mesoscale Urban Modelling*.
   Zenodo.
   https://doi.org/10.5281/zenodo.7298393

2. Zanaga, D., Van De Kerchove, R., Daems, D., et al. (2022).
   *ESA WorldCover 10 m 2021 v200*.
   https://doi.org/10.5281/zenodo.7254221

3. Powers, J. G., Klemp, J. B., Skamarock, W. C., et al. (2017).
   *The Weather Research and Forecasting Model: Overview, System Efforts, and Future Directions*.
   Bulletin of the American Meteorological Society, 98(8), 1717–1737.
