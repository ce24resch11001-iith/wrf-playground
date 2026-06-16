# Common Installation Pitfalls and Solutions for WRF & WPS

This guide summarizes common issues encountered while installing and compiling WRF and WPS on Linux and HPC systems.

---

## 1. NetCDF Not Found

### Error

```bash
netcdf.inc not found
```

or

```bash
cannot find -lnetcdf
```

### Solution

Verify the NetCDF environment variable:

```bash
echo $NETCDF
```

Check that NetCDF is properly installed:

```bash
nc-config --all
nf-config --all
```

Confirm the presence of required directories:

```bash
ls $NETCDF/include
ls $NETCDF/lib
```

---

## 2. HDF5 Library Errors

### Error

```bash
cannot find -lhdf5
```

or

```bash
HDF5 libraries not found
```

### Solution

Verify:

```bash
echo $HDF5
```

Check installation:

```bash
ls $HDF5/include
ls $HDF5/lib
```

Ensure HDF5 was compiled using the same compiler and MPI environment as NetCDF.

---

## 3. WPS Cannot Find Jasper Libraries

### Error

```bash
Cannot find jasper libraries
```

or

```bash
GRIB2 support not available
```

### Solution

Export:

```bash
export JASPERLIB=/path/to/lib
export JASPERINC=/path/to/include
```

Verify:

```bash
ls $JASPERLIB/libjasper*
ls $JASPERINC/jasper*
```

Reconfigure WPS after setting the variables.

---

## 4. Missing GRIB2 Support

### Symptom

Only `geogrid.exe` is created while `ungrib.exe` fails to compile.

### Solution

Verify:

```bash
echo $JASPERLIB
echo $JASPERINC
```

Then rebuild WPS:

```bash
./clean
./configure
./compile
```

---

## 5. WRF Compilation Fails

### Symptom

Compilation stops before generating executables.

### Solution

Inspect the compilation log:

```bash
grep -i error compile.log
```

Verify compiler configuration:

```bash
which gcc
which gfortran
which mpicc
which mpif90
```

Ensure all libraries were built using the same compiler family.

---

## 6. Missing WRF Executables After Compilation

### Symptom

One or more expected executables are missing:

```text
real.exe
wrf.exe
ndown.exe
tc.exe
```

### Solution

Check the final lines of:

```bash
compile.log
```

Look for the first compilation error and resolve it before recompiling.

---

## 7. Missing WPS Executables After Compilation

### Symptom

One or more expected executables are missing:

```text
geogrid.exe
ungrib.exe
metgrid.exe
```

### Solution

Review:

```bash
grep -i error configure.wps
grep -i error compile.log
```

Verify Jasper and NetCDF paths.

---

## 8. Compiler Mismatch

### Symptom

Compilation errors occur even though dependencies are installed.

### Cause

Libraries were compiled using different compiler versions.

### Solution

Verify:

```bash
which gcc
which gfortran
gcc --version
gfortran --version
```

Compile all dependencies, WRF, and WPS using the same compiler environment.

---

## 9. MPI Configuration Issues

### Error

```bash
mpif90 not found
```

or

```bash
MPI compilation failed
```

### Solution

Load MPI modules:

```bash
module load openmpi
```

Verify:

```bash
which mpif90
mpif90 --version
```

---

## 10. Environment Variables Not Set

### Symptom

WRF or WPS cannot locate required libraries.

### Solution

Verify:

```bash
echo $NETCDF
echo $HDF5
echo $JASPERLIB
echo $JASPERINC
```

Ensure all paths point to the correct installation directories.

---

## Recommended Pre-Compilation Checks

Before compiling WRF or WPS, verify:

```bash
which gcc
which gfortran
which mpicc
which mpif90

nc-config --all
nf-config --all

echo $NETCDF
echo $HDF5
echo $JASPERLIB
echo $JASPERINC
```

---

## Final Verification

### WRF

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

### WPS

```bash
ls *.exe
```

Expected:

```text
geogrid.exe
ungrib.exe
metgrid.exe
```

If all executables are present, the installation was successful.

## 11. WRF-Chem Not Enabled

### Symptom

WRF compiles successfully, but chemistry options are unavailable or chemistry-related files are not compiled.

### Solution

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

After running `./configure`, verify:

```bash
grep WRF_CHEM configure.wrf
```

Expected output should contain:

```text
WRF_CHEM = 1
-DWRF_CHEM
-DWRF_KPP
```

If chemistry support is missing, export the variables again and rerun:

```bash
./configure
```

---

## 12. Flex Not Found During WRF-Chem Compilation

### Error

```bash
flex: command not found
```

or

```bash
lex.yy.c generation failed
```

### Solution

Verify:

```bash
which flex
flex --version
```

If using a local Flex installation:

```bash
export FLEX=/path/to/flex
export FLEX_LIB_DIR=/path/to/lib
export PATH=/path/to/bin:$PATH
```

Reconfigure and recompile WRF-Chem after correcting the Flex path.

---

## 13. Dirty Source Tree After Failed Compilation

### Symptom

Compilation continues to fail even after fixing the original problem.

### Cause

Old object files and module files remain from a previous failed build.

### Solution

Clean the source tree completely:

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

A clean rebuild often resolves persistent compilation issues.

---

## 14. Mixed MPI Environments

### Symptom

Compilation succeeds, but linking fails or executables crash at runtime.

### Cause

Libraries were compiled using one MPI implementation while WRF was compiled using another.

Examples:

```text
OpenMPI + Intel MPI
MPICH + OpenMPI
```

### Solution

Verify:

```bash
which mpicc
which mpif90

mpicc --version
mpif90 --version
```

Ensure NetCDF, HDF5, WRF, and WPS were all built using the same MPI wrappers and compiler family.

Avoid mixing MPI implementations within the same software stack.

