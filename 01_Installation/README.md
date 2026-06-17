# 01_Installation and Compilation

This section contains installation and compilation workflows for the Weather Research and Forecasting (WRF) system, WRF-Chem, and supporting components.

## Available Guides

1. **Build WRF 4.7.1 + WPS 4.6.0**

   Step-by-step guide for compiling WRF 4.7.1 and WPS 4.6.0 with GNU compilers, MPI, NetCDF, HDF5, Jasper, and LibPNG on Linux/HPC systems.

   * File: `wrf4.7.1_wps4.6.0_build.md`

2. **Build WRF-Chem 4.7.1 + WPS 4.6.0**

   Guide for compiling WRF-Chem 4.7.1 with chemistry and KPP support, along with required dependencies (Flex, Zlib, HDF5, NetCDF-C, NetCDF-Fortran, Jasper, and LibPNG).

   * File: `wrfchem4.7.1_wps4.6.0_build.md`

3. **Runtime Environment Setup**

   Before running WRF, WRF-Chem, or WPS on an HPC system, source:

   * File: `wrf_env.sh`

   This file restores required environment variables and library paths (NetCDF, HDF5, Jasper, etc.) for the current HPC session.

   Since environment variables are session-specific, source this file after every new HPC login:

   ```bash
   source wrf_env.sh

## Notes

* Always verify compiler, MPI, and library compatibility before compilation.
* Follow the guides in the order presented.
* Build and validate all prerequisite libraries before compiling WRF or WRF-Chem.
* For WRF-Chem installations, ensure that chemistry and KPP support are enabled during configuration.
* Refer to troubleshooting documentation for common installation issues (`common_errors.md`).
