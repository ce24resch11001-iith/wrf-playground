#!/bin/bash

export DIR=/home/hwre1/ce24resch11001/WRF_BUILD

export NETCDF=$DIR/Libs
export HDF5=$DIR/Libs
export JASPERLIB=$DIR/Libs/lib
export JASPERINC=$DIR/Libs/include

export LD_LIBRARY_PATH=$NETCDF/lib:$LD_LIBRARY_PATH
export PATH=$NETCDF/bin:$PATH

