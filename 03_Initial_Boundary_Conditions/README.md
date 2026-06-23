# 03_Initial_Boundary_Conditions

Initial and Boundary Condition (ICBC) datasets provide the large-scale atmospheric information required to initialize and drive Weather Research and Forecasting (WRF) simulations. The choice of forcing dataset influences model performance, computational requirements, and suitability for specific research applications.

This section documents practical workflows for obtaining, preparing, and using commonly employed atmospheric forcing datasets within WRF and WPS environments.

---

## Overview

WRF simulations require:

* Initial Conditions (IC) to define the atmospheric state at the simulation start time.
* Boundary Conditions (BC) to continuously update meteorological fields along the model boundaries throughout the simulation period.

These datasets are typically obtained from global atmospheric reanalysis products or operational forecast systems.

---

## Contents

### ERA5 Reanalysis

ERA5, produced by the European Centre for Medium-Range Weather Forecasts (ECMWF), is one of the most widely used datasets for atmospheric and climate research.

Topics covered:

* ERA5 data acquisition
* CDS API setup
* Variable selection
* Pressure-level and single-level products
* Conversion for WPS processing
* WRF initialization using ERA5

Directory:

```text
03_Initial_Boundary_Conditions/
└── ERA5/
```

---

### FNL (Final Operational Global Analysis)

The NCEP Final Analysis (FNL) dataset provides global atmospheric analyses at regular intervals and is commonly used for weather and regional climate simulations.

Topics covered:

* FNL data download
* GRIB file handling
* WPS preprocessing
* Integration with WRF

Directory:

```text
03_Initial_Boundary_Conditions/
└── FNL/
```

---

### GFS Forecast Data

The Global Forecast System (GFS) provides operational forecast fields suitable for both research and forecasting applications.

Topics covered:

* GFS data acquisition
* Forecast cycle selection
* WPS preprocessing
* Forecast-oriented simulations

Directory:

```text
03_Initial_Boundary_Conditions/
└── GFS/
```

---

## Typical Workflow

The general workflow for using atmospheric forcing datasets within WRF is:

```text
Global Dataset
      ↓
Data Download
      ↓
WPS Ungrib
      ↓
Metgrid Processing
      ↓
real.exe
      ↓
wrf.exe
```

---

## Dataset Selection Guidance

| Dataset | Type       | Typical Resolution | Common Applications                                 |
| ------- | ---------- | ------------------ | --------------------------------------------------- |
| ERA5    | Reanalysis | ~31 km             | Climate, urban climate, aerosols, long-term studies |
| FNL     | Analysis   | ~25 km             | Weather events, case studies                        |
| GFS     | Forecast   | Variable           | Forecasting and operational applications            |

---

## Notes

* Dataset availability, resolution, and formats may change as data providers update their services.
* Users should verify variable requirements and temporal coverage before downloading large datasets.
* The workflows provided in this repository are based on practical WRF applications conducted on Linux and HPC environments.

---

## Future Additions

Planned additions include:

* Automated ERA5 download scripts
* CDS API setup guides
* Batch download workflows
* HPC-oriented preprocessing pipelines
* Comparison of ERA5, FNL, and GFS forcing datasets
* MPAS forcing data preparation examples

---

## Repository Context

This section forms part of the WRF-Playground project, which aims to document reproducible workflows for atmospheric, urban climate, and environmental modeling using the Weather Research and Forecasting (WRF) system.
