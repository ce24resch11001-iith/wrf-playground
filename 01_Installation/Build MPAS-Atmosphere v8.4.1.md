# Build MPAS-Atmosphere v8.4.1

This guide documents the compilation and installation of MPAS-Atmosphere v8.4.1 using GNU compilers and OpenMPI on Linux/HPC systems.

The workflow builds:

- `init_atmosphere_model` (MPAS preprocessing core)
- `atmosphere_model` (MPAS-Atmosphere simulation core)

---

# Tested Configuration

| Component | Version |
|------------|---------|
| GCC | System Module |
| OpenMPI | System Module |
| Zlib | 1.3.1 |
| HDF5 | 1.13.2 |
| NetCDF-C | 4.9.0 |
| NetCDF-Fortran | 4.6.0 |
| Parallel-NetCDF | 1.12.3 |
| MPAS-Model | v8.4.1 |

---

# Before Starting

Load required modules:

```bash
module purge

module load gcc
module load openmpi
module load cmake
````

Check compilers:

```bash
which gcc
which gfortran
which mpicc
which mpif90

gcc --version
gfortran --version
mpif90 --version
```

---

# Workspace Setup

Create MPAS build directory:

```bash
export SCRATCH=$HOME

mkdir -p $SCRATCH/MPAS_BUILD/{Downloads,Libs}

export MPAS_HOME=$SCRATCH/MPAS_BUILD
export DIR=$MPAS_HOME/Libs

cd $MPAS_HOME
```

Directory structure:

```
MPAS_BUILD
|
├── Downloads
|
├── Libs
|
└── MPAS-Model-v8.4.1
```

---

# Compiler Environment

```bash
export CC=gcc
export CXX=g++
export FC=gfortran
export F77=gfortran

export PATH=$DIR/bin:$PATH
export LD_LIBRARY_PATH=$DIR/lib:$LD_LIBRARY_PATH

export NETCDF=$DIR
export PNETCDF=$DIR

ulimit -s unlimited
```

---

# Build ZLIB 1.3.1

```bash
cd $MPAS_HOME/Downloads

wget -nc https://www.zlib.net/zlib-1.3.1.tar.gz

tar -xzf zlib-1.3.1.tar.gz

cd zlib-1.3.1

./configure --prefix=$DIR

make -j8
make install
```

---

# Build HDF5 1.13.2

```bash
cd $MPAS_HOME/Downloads

wget -nc \
https://support.hdfgroup.org/ftp/HDF5/releases/hdf5-1.13/hdf5-1.13.2/src/hdf5-1.13.2.tar.gz

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

# Build NetCDF-C 4.9.0

```bash
cd $MPAS_HOME/Downloads

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

# Build NetCDF-Fortran 4.6.0

```bash
cd $MPAS_HOME/Downloads

wget -nc \
https://downloads.unidata.ucar.edu/netcdf-fortran/4.6.0/netcdf-fortran-4.6.0.tar.gz


tar -xzf netcdf-fortran-4.6.0.tar.gz


cd netcdf-fortran-4.6.0


export CPPFLAGS="-I$DIR/include"
export LDFLAGS="-L$DIR/lib"


./configure \
--prefix=$DIR


make -j8

make install
```

---

# Build Parallel-NetCDF 1.12.3

MPAS requires Parallel-NetCDF for parallel I/O.

```bash
cd $MPAS_HOME/Downloads


wget -nc \
https://parallel-netcdf.github.io/Release/pnetcdf-1.12.3.tar.gz


tar -xzf pnetcdf-1.12.3.tar.gz


cd pnetcdf-1.12.3


CC=mpicc FC=mpif90 ./configure \
--prefix=$DIR


make -j8


make install
```

---

# Export All Variables

After installation, reload environment:

```bash
module purge

module load gcc
module load openmpi
module load cmake


export CC=gcc
export CXX=g++
export FC=gfortran
export F77=gfortran


export MPAS_HOME=$HOME/MPAS_BUILD
export DIR=$MPAS_HOME/Libs


export PATH=$DIR/bin:$PATH
export LD_LIBRARY_PATH=$DIR/lib:$LD_LIBRARY_PATH


export NETCDF=$DIR
export PNETCDF=$DIR


ulimit -s unlimited
```

---

# Verify Libraries

Check compilers:

```bash
which gcc
which gfortran
which mpicc
which mpif90
```

Check NetCDF:

```bash
nc-config --version

nf-config --version
```

Check Parallel-NetCDF:

```bash
nc-config --all

mpif90 --version
```

Check PNetCDF:

```bash
ls $DIR/lib | grep pnetcdf
```

Expected:

```
libpnetcdf.a
libpnetcdf.so
```

---

# Download MPAS-Model v8.4.1

```bash
cd $MPAS_HOME


wget -nc \
https://github.com/MPAS-Dev/MPAS-Model/archive/refs/tags/v8.4.1.tar.gz \
-O MPAS-v8.4.1.tar.gz


tar -xzf MPAS-v8.4.1.tar.gz


cd MPAS-Model-v8.4.1
```

---

# Compile init_atmosphere Core

MPAS uses the same source tree for multiple cores.

Compile preprocessing core:

```bash
make -j8 gnu CORE=init_atmosphere \
2>&1 | tee init_compile.log
```

Successful compilation creates:

```bash
ls -lh init_atmosphere_model
```

Expected:

```
-rwxr-xr-x init_atmosphere_model
```

---

# Compile Atmosphere Core

Compile main MPAS atmospheric model:

```bash
make -j8 gnu CORE=atmosphere \
2>&1 | tee atmosphere_compile.log
```

Successful compilation creates:

```bash
ls -lh atmosphere_model
```

Expected:

```
-rwxr-xr-x atmosphere_model
```

---

# Verify MPAS Installation

Check executables:

```bash
ls -lh init_atmosphere_model

ls -lh atmosphere_model
```

Expected:

```
init_atmosphere_model
atmosphere_model
```

---

# Check Generated Files

After compilation:

```bash
ls
```

Expected important files:

```
init_atmosphere_model
atmosphere_model

namelist.init_atmosphere
streams.init_atmosphere

namelist.atmosphere
streams.atmosphere

build_tables
```

---

# Compilation Summary

Successful MPAS build produces:

## MPAS Initialization Core

```
init_atmosphere_model
```

Used for:

* mesh preparation
* static fields
* meteorological preprocessing

---

## MPAS Atmosphere Core

```
atmosphere_model
```

Used for:

* weather simulations
* climate simulations
* regional atmospheric studies

---

# Final Environment Check

```bash
echo $NETCDF

echo $PNETCDF

which mpif90

mpif90 --version

ls -lh init_atmosphere_model

ls -lh atmosphere_model
```

MPAS-Atmosphere v8.4.1 installation is complete.

```
