#!/bin/bash

export DIR= path/to/WRF_BUILD

export NETCDF=$DIR/Libs
export HDF5=$DIR/Libs
export JASPERLIB=$DIR/Libs/lib
export JASPERINC=$DIR/Libs/include

export LD_LIBRARY_PATH=$NETCDF/lib:$LD_LIBRARY_PATH
export PATH=$NETCDF/bin:$PATH

