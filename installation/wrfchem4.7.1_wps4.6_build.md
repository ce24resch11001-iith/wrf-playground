# Build WRF-Chem 4.7.1 + WPS 4.6.0

This guide documents the compilation and installation of WRF-Chem 4.5 and WPS 4.5 using GNU compilers and MPI wrappers available on Linux/HPC systems.

## Tested Configuration

| Component      | Version                           |
| -------------- | --------------------------------- |
| GCC            | System GCC                        |
| MPI            | Intel MPI wrappers (mpicc/mpif90) |
| Flex           | 2.6.4                             |
| Zlib           | 1.2.13                            |
| HDF5           | 1.13.2                            |
| NetCDF-C       | 4.9.0                             |
| NetCDF-Fortran | 4.6.0                             |
| Jasper         | 1.900.1                           |
| LibPNG         | 1.6.39                            |
| WRF-Chem       | 4.5                               |
| WPS            | 4.5                               |

---

## Before Starting

```bash
which gcc
which gfortran
which mpicc
which mpif90
which flex

gcc --version
gfortran --version
mpif90 --version
flex --version
```

---

## Workspace Setup

```bash
export SCRATCH=$(pwd)

mkdir -p $SCRATCH/WRF_CHEM_BUILD/{Downloads,Libs}

export WRFCHEM_HOME=$SCRATCH/WRF_CHEM_BUILD
export DIR=$WRFCHEM_HOME/Libs

cd $WRFCHEM_HOME
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


# Build FLEX
```bash

cd $WRFCHEM_HOME/Downloads

wget -nc https://github.com/westes/flex/releases/download/v2.6.4/flex-2.6.4.tar.gz

tar -xzf flex-2.6.4.tar.gz

cd flex-2.6.4

./configure --prefix=$DIR

make -j8
make install

export FLEX=$DIR/bin/flex
export FLEX_LIB_DIR=$DIR/lib
```
---

# Build ZLIB

```bash
cd $WRFCHEM_HOME/Downloads

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
cd $WRFCHEM_HOME/Downloads

wget -nc \
https://support.hdfgroup.org/ftp/HDF5/releases/hdf5-1.13/hdf5-1.13.2/src/hdf5-1.13.2.tar.gz

tar -xzf hdf5-1.13.2.tar.gz

cd hdf5-1.13.2

CC=mpicc FC=mpif90 ./configure \
 --prefix=$DIR \
 --enable-parallel \
 --enable-fortran \
 --with-zlib=$DIR

make -j8
make install

export HDF5=$DIR
```

---

# Build NetCDF-C

```bash
cd $WRFCHEM_HOME/Downloads

wget -nc \
https://github.com/Unidata/netcdf-c/archive/refs/tags/v4.9.0.tar.gz

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
cd $WRFCHEM_HOME/Downloads

wget -nc \
https://downloads.unidata.ucar.edu/netcdf-fortran/4.6.0/netcdf-fortran-4.6.0.tar.gz

tar -xzf netcdf-fortran-4.6.0.tar.gz

cd netcdf-fortran-4.6.0

export CPPFLAGS="-I$DIR/include"
export LDFLAGS="-L$DIR/lib"

./configure --prefix=$DIR

make -j8
make install

export NETCDF=$DIR
```

---

# Build Jasper

```bash
cd $WRFCHEM_HOME/Downloads

wget -nc \
http://www.ece.uvic.ca/~mdadams/jasper/software/jasper-1.900.1.zip

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
cd $WRFCHEM_HOME/Downloads

wget -nc \
https://download.sourceforge.net/libpng/libpng-1.6.39.tar.gz

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

# Build WRF-Chem 4.7.1

```bash
cd $WRFCHEM_HOME/Downloads

wget -nc \
https://github.com/wrf-model/WRF/releases/download/v4.7.1/v4.7.1.tar.gz \
-O wrf-4.7.1.tar.gz

tar -xzf wrf-4.7.1.tar.gz -C $WRFCHEM_HOME

cd $WRFCHEM_HOME/WRFV4.7.1
```

## Enable Chemistry

```bash
export WRF_EM_CORE=1
export WRF_NMM_CORE=0

export WRF_CHEM=1
export WRF_KPP=1

export YACC='/usr/bin/yacc -d'

export KPP_HOME=$WRFCHEM_HOME/WRFV4.7.1/chem/KPP/kpp/kpp-2.1

export PATH=$KPP_HOME/bin:$PATH

export WRFIO_NCD_LARGE_FILE_SUPPORT=1
```

## Configure KPP

```bash
cd chem/KPP

sed -i 's/="-O"/="-O0"/' configure_kpp

cd ../..
```

## Configure

```bash
./configure
```

Choose:

```text
34 = GNU (gfortran/gcc), dmpar
1 = basic nesting (default)
```

## Compile

```bash
./compile em_real 2>&1 | tee wrfchem_compile.log
```

---

## Verify WRF-Chem

```bash
export WRF_DIR=$WRFCHEM_HOME/WRFV4.7.1

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

# Build Emission Converter

```bash
cd $WRFCHEM_HOME/WRFV4.7.1

./compile emi_conv 2>&1 | tee emission_compile.log
```

---

# Build WPS 4.6.0

```bash
cd $WRFCHEM_HOME/Downloads

wget -nc \
https://github.com/wrf-model/WPS/archive/refs/tags/v4.6.0.tar.gz \
-O wps-4.6.0.tar.gz

tar -xzf wps-4.6.0.tar.gz -C $WRFCHEM_HOME

cd $WRFCHEM_HOME/WPS-4.6.0

export WRF_DIR=$WRFCHEM_HOME/WRFV4.7.1

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

ls $WRFCHEM_HOME/WPS-4.6.0/*.exe
```

You are finished when all of the following exist.

## WRF-Chem

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
