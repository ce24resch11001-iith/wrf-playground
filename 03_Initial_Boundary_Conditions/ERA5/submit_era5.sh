#!/bin/bash
#SBATCH --job-name=ERA5
#SBATCH --output=era5_job.out
#SBATCH --error=era5_job.err

#SBATCH --partition=speed
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1

#SBATCH --time=24:00:00

module load python

python era5_surface_same_months.py
python era5_pressure_same_months.py
#python era5_surface_consecutive_months.py
#python era5_pressure_consecutive_months.py
