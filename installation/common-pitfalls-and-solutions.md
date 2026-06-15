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
