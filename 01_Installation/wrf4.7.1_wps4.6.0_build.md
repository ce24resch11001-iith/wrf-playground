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
Check:
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

```
---

## Workspace Setup

```bash
export SCRATCH=$(pwd)

mkdir -p $SCRATCH/WRF_BUILD/{Downloads,Libs}

export WRF_HOME=$SCRATCH/WRF_BUILD
export DIR=$WRF_HOME/Libs

cd $WRF_HOME
```

---

## Compiler Environment

```bash
export CC=gcc
export CXX=g++
export FC=gfortran
export F77=gfortran

export PATH=$DIR/bin:$PATH
export LD_LIBRARY_PATH=$DIR/lib:$LD_LIBRARY_PATH

export NETCDF=$DIR
export HDF5=$DIR

ulimit -s unlimited
```

---

# Build ZLIB

```bash
cd $WRF_HOME/Downloads

wget -nc https://www.zlib.net/fossils/zlib-1.2.13.tar.gz

tar -xzf zlib-1.2.13.tar.gz

cd zlib-1.2.13

./configure --prefix=$DIR

make -j8
make install
```

---

# Build HDF5

```bash
cd $WRF_HOME/Downloads

wget -nc https://support.hdfgroup.org/ftp/HDF5/releases/hdf5-1.13/hdf5-1.13.2/src/hdf5-1.13.2.tar.gz

tar -xzf hdf5-1.13.2.tar.gz

cd hdf5-1.13.2

CC=mpicc FC=mpif90 ./configure \
 --prefix=$DIR \
 --enable-fortran \
 --enable-parallel \
 --with-zlib=$DIR

make -j8
make install
```

---

# Build NetCDF-C

```bash
cd $WRF_HOME/Downloads

wget -nc https://github.com/Unidata/netcdf-c/archive/refs/tags/v4.9.0.tar.gz

tar -xzf v4.9.0.tar.gz

cd netcdf-c-4.9.0

export CPPFLAGS="-I$DIR/include"
export LDFLAGS="-L$DIR/lib"

./configure \
 --prefix=$DIR \
 --disable-dap

make -j8
make install
```

---

# Build NetCDF-Fortran

```bash
cd $WRF_HOME/Downloads

wget -nc https://downloads.unidata.ucar.edu/netcdf-fortran/4.6.0/netcdf-fortran-4.6.0.tar.gz

tar -xzf netcdf-fortran-4.6.0.tar.gz

cd netcdf-fortran-4.6.0

export CPPFLAGS="-I$DIR/include"
export LDFLAGS="-L$DIR/lib"

./configure --prefix=$DIR

make -j8
make install
```

---

# Build Jasper

```bash
cd $WRF_HOME/Downloads

wget -nc http://www.ece.uvic.ca/~mdadams/jasper/software/jasper-1.900.1.zip

unzip -o jasper-1.900.1.zip

cd jasper-1.900.1

autoreconf -i

./configure --prefix=$DIR

make -j8
make install
```

---

# Build LibPNG

```bash
cd $WRF_HOME/Downloads

wget -nc https://download.sourceforge.net/libpng/libpng-1.6.39.tar.gz

tar -xzf libpng-1.6.39.tar.gz

cd libpng-1.6.39

./configure --prefix=$DIR

make -j8
make install
```

---

## Export WPS Variables

```bash
export JASPERLIB=$DIR/lib
export JASPERINC=$DIR/include
```

---

## Verify Libraries

```bash
which nc-config
which nf-config

nc-config --all
nf-config --all

mpif90 --version
```

---

# Build WRF 4.7.1

```bash
cd $WRF_HOME/Downloads

wget -nc \
https://github.com/wrf-model/WRF/releases/download/v4.7.1/v4.7.1.tar.gz \
-O wrf-4.7.1.tar.gz

tar -xzf wrf-4.7.1.tar.gz -C $WRF_HOME

cd $WRF_HOME/WRFV4.7.1
```

## Configure

```bash
./configure
```

Choose:

```text
34 = GNU (gfortran/gcc), dmpar
1  = basic nesting
```

## Compile

```bash
./compile em_real 2>&1 | tee wrf_compile.log
```

Expected compile time: **30–90 minutes**, depending on cluster hardware.

---

## Verify WRF

```bash
export WRF_DIR=$WRF_HOME/WRFV4.7.1

ls -lah main/*.exe
```

Expected:

```text
real.exe
wrf.exe
ndown.exe
tc.exe
```

---

# Build WPS 4.6.0

```bash
cd $WRF_HOME/Downloads

wget -nc \
https://github.com/wrf-model/WPS/archive/refs/tags/v4.6.0.tar.gz \
-O wps-4.6.0.tar.gz

tar -xzf wps-4.6.0.tar.gz -C $WRF_HOME

cd $WRF_HOME/WPS-4.6.0

export WRF_DIR=$WRF_HOME/WRFV4.7.1
```

## Configure

```bash
./configure
```

Choose:

```text
Linux x86_64, gfortran, dmpar
```

## Compile

```bash
./compile 2>&1 | tee wps_compile.log
```

---

## Verify WPS

```bash
ls -lah *.exe
```

Expected:

```text
geogrid.exe
ungrib.exe
metgrid.exe
```

---

# Final Verification

```bash
nc-config --all

nf-config --all

mpif90 --version

ls $WRF_DIR/main/*.exe

ls $WRF_HOME/WPS-4.6.0/*.exe
```

You are finished when all of the following exist.

## WRF

```text
real.exe
wrf.exe
ndown.exe
tc.exe
```

## WPS

```text
geogrid.exe
ungrib.exe
metgrid.exe
```
