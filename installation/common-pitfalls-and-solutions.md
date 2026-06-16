# Common Installation Pitfalls and Solutions for WRF, WRF-Chem & WPS

This guide summarizes common issues encountered while installing and compiling WRF, WRF-Chem, and WPS on Linux and HPC systems.

---

# 1. NetCDF Not Found

## Error

```bash
netcdf.inc not found
```

or

```bash
cannot find -lnetcdf
```

## Solution

Verify:

```bash
echo $NETCDF

nc-config --all
nf-config --all

ls $NETCDF/include
ls $NETCDF/lib
```

Ensure NetCDF-C and NetCDF-Fortran were installed successfully and that `$NETCDF` points to the correct location.

---

# 2. HDF5 Library Errors

## Error

```bash
cannot find -lhdf5
```

or

```bash
HDF5 libraries not found
```

## Solution

Verify:

```bash
echo $HDF5

ls $HDF5/include
ls $HDF5/lib
```

HDF5 should be built using the same compiler and MPI environment used for NetCDF and WRF.

---

# 3. Jasper and GRIB2 Support Issues

## Error

```bash
Cannot find jasper libraries
```

or

```bash
GRIB2 support not available
```

## Solution

Verify:

```bash
echo $JASPERLIB
echo $JASPERINC

ls $JASPERLIB/libjasper*
ls $JASPERINC/jasper*
```

Export if necessary:

```bash
export JASPERLIB=/path/to/lib
export JASPERINC=/path/to/include
```

Then rebuild WPS:

```bash
./clean
./configure
./compile
```

If only `geogrid.exe` is created while `ungrib.exe` fails, the issue is usually related to Jasper or GRIB2 support.

---

# 4. WRF-Chem Not Enabled

## Issue

WRF compiles successfully but chemistry options are unavailable or chemistry-related files are not compiled.

## Solution

Verify:

```bash
echo $WRF_CHEM
echo $WRF_KPP
```

Expected:

```text
1
1
```

Check:

```bash
grep WRF_CHEM configure.wrf
```

Expected:

```text
WRF_CHEM = 1
-DWRF_CHEM
-DWRF_KPP
```

If chemistry support is missing:

```bash
export WRF_CHEM=1
export WRF_KPP=1

./configure
```

---

# 5. Flex Not Found During WRF-Chem Compilation

## Error

```bash
flex: command not found
```

or

```bash
lex.yy.c generation failed
```

## Solution

Verify:

```bash
which flex
flex --version
```

If using a local installation:

```bash
export FLEX=/path/to/flex
export FLEX_LIB_DIR=/path/to/lib
export PATH=/path/to/bin:$PATH
```

Reconfigure and recompile after correcting the Flex path.

---

# 6. Compiler and MPI Mismatch

## Error

Compilation, linking, or runtime failures occur despite successful dependency installation.

## Common Causes

* Libraries built with different compiler versions
* Libraries built with different MPI implementations
* MPI wrappers pointing to unexpected compilers

Examples:

```text
OpenMPI + Intel MPI
MPICH + OpenMPI
GCC 8 libraries + GCC 12 WRF build
```

## Solution

Verify:

```bash
which gcc
which gfortran

gcc --version
gfortran --version

which mpicc
which mpif90

mpicc --version
mpif90 --version
```

Check WRF configuration:

```bash
grep "^SCC" configure.wrf
grep "^SFC" configure.wrf
grep "^DM_FC" configure.wrf
```

Expected:

```text
SCC = gcc
SFC = gfortran
DM_FC = mpif90 -f90=$(SFC)
```

Build NetCDF, HDF5, WRF, and WPS using a consistent compiler and MPI stack.

---

# 7. Environment Variables Not Set

## Error

WRF or WPS cannot locate required libraries.

## Solution

Verify:

```bash
echo $NETCDF
echo $HDF5
echo $JASPERLIB
echo $JASPERINC
echo $FLEX
```

If necessary:

```bash
export NETCDF=/path/to/Libs
export HDF5=/path/to/Libs

export JASPERLIB=/path/to/Libs/lib
export JASPERINC=/path/to/Libs/include

export FLEX=/path/to/Libs/bin/flex
```

Consider storing them in:

```bash
~/.bashrc
```

or

```bash
~/wrf_env.sh
```

and sourcing them before compilation.

---

# 8. Dirty Source Tree After Failed Compilation

## Error

Compilation continues to fail even after the original problem has been fixed.

## Cause

Old object files, module files, or dependency information remain from a previous build.

## Solution

Perform a complete cleanup:

```bash
./clean -a

find . -name "*.o" -delete
find . -name "*.mod" -delete
```

Then rerun:

```bash
./configure
./compile em_real
```

This is especially important after changing:

* Compiler versions
* MPI implementations
* NetCDF installations
* HDF5 installations
* WRF-Chem settings
* KPP settings

---

# 9. Missing Chemistry Source Dependencies

## Error

```bash
No rule to make target 'chem/module_input_tracer.o'
```

or

```bash
No rule to make target 'chem/module_input_tracer_data.o'
```

or

```bash
No rule to make target 'chem/module_data_mosaic_asect.o'
```

## Solution

Verify source files exist:

```bash
find chem -name "module_input_tracer*"

find chem -name "module_data_mosaic_asect*"
```

Expected:

```text
chem/module_input_tracer.F
chem/module_input_tracer_data.F
chem/module_data_mosaic_asect.F
chem/module_data_mosaic_asecthp.F
```

If files exist, perform a complete clean build:

```bash
./clean -a

find . -name "*.o" -delete
find . -name "*.mod" -delete

./configure
./compile em_real
```

These errors are commonly caused by stale dependency information.

---

# 10. Compilation Completes but Executables Are Missing

## Error

One or more expected executables are not created.

### WRF

Expected:

```text
real.exe
wrf.exe
ndown.exe
tc.exe
```

### WPS

Expected:

```text
geogrid.exe
ungrib.exe
metgrid.exe
```

## Solution

Search for the first actual error:

```bash
grep -ni "error" wrfchem_compile.log | head -50
```

or

```bash
grep -ni "error" compile.log | head -50
```

The first error is usually the root cause. Later errors are often secondary failures.

---

# Recommended Pre-Compilation Checks

Before launching a long compilation:

```bash
which gcc
which gfortran
which mpicc
which mpif90

gcc --version
gfortran --version

mpif90 --version

which flex
flex --version

nc-config --all
nf-config --all

echo $NETCDF
echo $HDF5
echo $JASPERLIB
echo $JASPERINC
echo $WRF_CHEM
echo $WRF_KPP
```

Also verify:

```bash
grep WRF_CHEM configure.wrf

grep "^SCC" configure.wrf
grep "^SFC" configure.wrf
grep "^DM_FC" configure.wrf
```

Confirm:

```text
WRF_CHEM = 1
WRF_KPP enabled
Correct NetCDF paths
Correct HDF5 paths
Correct Jasper paths
Flex available
MPI wrappers available
Expected compiler configuration
```

---

# Final Verification

## WRF

```bash
ls main/*.exe
```

Expected:

```text
real.exe
wrf.exe
ndown.exe
tc.exe
```

## WPS

```bash
ls *.exe
```

Expected:

```text
geogrid.exe
ungrib.exe
metgrid.exe
```

If all expected executables are present, the installation was successful.
