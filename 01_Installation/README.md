# Installation and Compilation

This section contains installation and compilation workflows for the Weather Research and Forecasting (WRF) modeling system, WRF-Chem, and supporting components.

## Available Guides

1. **Build WRF 4.7.1 + WPS 4.6.0**
   Comprehensive step-by-step guide for compiling WRF 4.7.1 and WPS 4.6.0 with GNU compilers, MPI, NetCDF, HDF5, Jasper, and LibPNG on Linux/HPC systems.

   * File: `wrf4.7.1_wps4.6.0_build.md`

2. **Build WRF-Chem 4.7.1 + WPS 4.6.0**
   Comprehensive guide for compiling WRF-Chem 4.7.1 with chemistry and KPP support, along with WPS 4.6.0 and all required dependencies (Flex, Zlib, HDF5, NetCDF-C, NetCDF-Fortran, Jasper, and LibPNG) on Linux/HPC systems.

   * File: `wrfchem4.7.1_wps4.6.0_build.md`

## Notes

* Always verify compiler, MPI, and library compatibility before compilation.
* Follow the guides in the order presented.
* Build and validate all prerequisite libraries before compiling WRF or WRF-Chem.
* For WRF-Chem installations, ensure that chemistry and KPP support are enabled during configuration.
* Refer to troubleshooting documentation for common installation issues (`common_errors.md`).
