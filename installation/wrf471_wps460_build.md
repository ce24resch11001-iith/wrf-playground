# Build WRF 4.7.1 + WPS 4.6.0

This guide documents the compilation and installation of WRF 4.7.1 and WPS 4.6.0 using GNU compilers and OpenMPI on Linux/HPC systems.

## Tested Configuration

| Component | Version |
|------------|---------|
| GCC | System Module |
| OpenMPI | System Module |
| Zlib | 1.2.13 |
| HDF5 | 1.13.2 |
| NetCDF-C | 4.9.0 |
| NetCDF-Fortran | 4.6.0 |
| Jasper | 1.900.1 |
| LibPNG | 1.6.39 |
| WRF | 4.7.1 |
| WPS | 4.6.0 |

---

## Before Starting

```bash
module purge

module load gcc
module load openmpi
module load cmake

which gcc
which gfortran
which mpicc
which mpif90

gcc --version
gfortran --version
mpif90 --version
