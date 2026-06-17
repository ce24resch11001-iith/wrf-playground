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

   Before running WRF, WRF-Chem, or WPS, source:

   * File: `wrf_env.sh`

   This file restores required environment variables and library paths (NetCDF, HDF5, Jasper, etc.) for the current session.

   On HPC systems, source this file after every new login session:

   ```bash
   source wrf_env.sh
   ````
   For local Linux installations, add the following line to `~/.bashrc` to load the environment automatically:

   ```bash
   source /path/to/wrf_env.sh
   ```

   Reload the shell after updating `.bashrc`:

   ```bash
   source ~/.bashrc
   ```

## Notes

* Verify compiler, MPI, and library compatibility before compilation.
* Follow the guides in the order presented.
* Build and validate prerequisite libraries before compiling WRF or WRF-Chem.
* Ensure chemistry and KPP support are enabled when building WRF-Chem.
* Refer to `common_errors.md` for troubleshooting.
