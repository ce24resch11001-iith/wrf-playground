# Common Pitfalls and Solutions in WRF & WPS

This document summarizes common issues encountered during the installation, configuration, compilation, preprocessing, and execution of WRF and WPS.

The solutions presented here are based on practical experience from Linux and HPC environments and may help users quickly diagnose and resolve common problems.

---

# 1. WRF Compilation Fails

## Problem

WRF compilation stops before generating executables such as:

```text
real.exe
wrf.exe
ndown.exe
tc.exe
```

## Possible Causes

* Incorrect compiler selection
* Missing NetCDF libraries
* Missing MPI libraries
* Environment variables not exported correctly
* Unsupported compiler versions

## Solution

Verify environment variables:

```bash
echo $NETCDF
echo $HDF5
which mpif90
which gcc
```

Check compilation log:

```bash
grep -i error compile.log
```

Ensure the following executables exist:

```bash
which nc-config
which nf-config
```

---

# 2. Missing `real.exe` or `wrf.exe`

## Problem

Compilation completes but:

```bash
ls main/*.exe
```

does not show all expected executables.

## Solution

Review the final lines of:

```bash
compile.log
```

Look specifically for:

```text
Compilation successful
```

If absent, identify the first compilation error and resolve it before recompiling.

---

# 3. WPS Cannot Find Jasper Libraries

## Problem

During WPS configuration:

```text
Cannot find jasper libraries
```

or

```text
grib2 support not available
```

## Solution

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

Reconfigure WPS afterwards.

---

# 4. geogrid.exe Builds but ungrib.exe Fails

## Problem

Only:

```text
geogrid.exe
```

is created.

## Possible Cause

Missing GRIB2 dependencies.

## Solution

Verify:

```bash
echo $JASPERLIB
echo $JASPERINC
```

Then clean and rebuild:

```bash
./clean
./configure
./compile
```

---

# 5. NetCDF Not Found During Compilation

## Problem

Compilation reports:

```text
netcdf.inc not found
```

or

```text
cannot find -lnetcdf
```

## Solution

Verify:

```bash
echo $NETCDF
```

Test:

```bash
nc-config --all
nf-config --all
```

Confirm:

```bash
ls $NETCDF/include
ls $NETCDF/lib
```

---

# 6. Segmentation Fault During real.exe

## Problem

Execution stops with:

```text
Segmentation fault
```

## Possible Causes

* Incorrect domain configuration
* Inconsistent namelist settings
* Insufficient memory

## Solution

Check:

```bash
rsl.error.0000
```

Verify:

* start_date
* end_date
* parent_grid_ratio
* e_we
* e_sn

Ensure domain dimensions are reasonable.

---

# 7. real.exe Completes but wrf.exe Fails

## Problem

Files generated:

```text
wrfinput_d01
wrfbdy_d01
```

but WRF crashes.

## Solution

Inspect:

```bash
rsl.error.*
```

Common causes:

* Memory exhaustion
* Physics option conflicts
* Incorrect time step

Recommended initial timestep:

```text
time_step ≈ 6 × grid spacing (km)
```

Example:

```text
3 km domain → 18 s
```

---

# 8. geogrid.exe Fails

## Problem

geogrid stops unexpectedly.

## Solution

Verify:

```bash
geog_data_path
```

Check that:

```bash
GEOGRID.TBL
```

matches the installed static datasets.

Confirm all required geographical datasets exist.

---

# 9. metgrid.exe Cannot Find Intermediate Files

## Problem

Error:

```text
Couldn't open intermediate file
```

## Solution

Verify:

```bash
ls FILE:*
```

If files are missing:

```bash
ungrib.exe
```

did not complete successfully.

Review:

```bash
ungrib.log
```

---

# 10. WRF Runs Extremely Slowly

## Possible Causes

* Too many processors
* Poor domain decomposition
* Excessive output frequency
* Oversized domains

## Recommendations

Test scaling using:

```bash
mpirun -np 4
mpirun -np 8
mpirun -np 16
```

Monitor:

```bash
tail rsl.out.0000
```

to evaluate simulation speed.

---

# 11. WPS Compilation Appears Successful but Executables Are Missing

## Solution

Verify:

```bash
ls *.exe
```

Expected:

```text
geogrid.exe
ungrib.exe
metgrid.exe
```

If missing:

```bash
grep -i error configure.wps
grep -i error compile.log
```

---

# 12. General Debugging Workflow

Whenever WRF or WPS fails:

1. Read the complete error message.
2. Check environment variables.
3. Verify libraries and dependencies.
4. Review log files.
5. Search for the first reported error, not the last one.
6. Rebuild from a clean state if necessary.

Useful files:

```text
compile.log
configure.wrf
configure.wps
rsl.error.0000
rsl.out.0000
geogrid.log
ungrib.log
metgrid.log
```

---

# Final Advice

Most WRF and WPS issues originate from one of the following:

* Environment variable misconfiguration
* Library incompatibility
* Incorrect namelist settings
* Missing static datasets
* MPI or compiler inconsistencies

Always verify each stage independently before proceeding to the next step in the workflow.
