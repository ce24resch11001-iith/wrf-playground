# wrf-playground

# WRF Workflows

A collection of practical, reproducible workflows for working with the Weather Research and Forecasting (WRF) model for atmospheric and climate research applications.

This repository serves as a hands-on reference for setting up, running, and analyzing WRF simulations based on real research workflows used in HPC and academic environments.

---

## Author

**Uppucharla Venkata Rohith**  
PhD Research Scholar  

Hydraulics and Water Resources Engineering (HWRE)  
Department of Civil Engineering  
Indian Institute of Technology Hyderabad, India  


Academic Portfolio: https://sites.google.com/view/uvrohith  

Lab Member: *Multidisciplinary Exploration of Geospatial Hydrometeorological Applications (MEGHA)*  

---

## Research Focus

My research focuses on understanding the interactions between:

- Urban heat island effects  
- Aerosol characteristics  
- Precipitation patterns over Indian cities  

This work uses:

- Weather Research and Forecasting (WRF) model  
- Remote sensing datasets  
- Machine learning techniques  

to investigate urban–atmosphere feedback mechanisms and their influence on regional climate and rainfall dynamics.

---

## What this repository covers

This repository documents end-to-end WRF workflows including:

### Model Setup & Installation
- WRF and WPS compilation on Linux/HPC systems  
- NetCDF, MPI, and dependency configuration  
- Common installation and runtime issues  

### Data Preprocessing
- ERA5 reanalysis processing for WRF input  
- NCEP FNL dataset usage  
- Vtable configuration  
- GRIB to intermediate file processing  

### WPS Workflow
- Domain setup using `geogrid`  
- `ungrib` and `metgrid` execution  
- Static dataset handling  
- Troubleshooting WPS errors  

### WRF Simulation Runs
- `real.exe` and `wrf.exe` execution  
- Namelist configuration  
- Nested domain setups  
- Debugging runtime issues  

### Physics Configurations
- Urban schemes (SLUCM and NO-URB cases)  
- Sensitivity experiments  
- Surface and boundary layer parameterization impacts  

### Post-processing
- WRF output (`wrfout`) analysis  
- Basic visualization workflows  
- Data extraction for research studies  

---

## Purpose of this repository

This repository is created to:

- Document real-world WRF workflows  
- Help researchers and students reproduce simulations  
- Provide structured references for common issues and solutions  
- Support transparent and reproducible atmospheric modeling research  

---

## Who this is for

This repository is useful for:

- Atmospheric science researchers  
- Students working with WRF or regional climate models  
- HPC users running WRF simulations  
- Beginners learning WRF step-by-step workflows  

---

## Important Note

This repository reflects practical research workflows and experimental configurations used in real atmospheric modeling studies. Results and setups may vary depending on system architecture, dataset versions, and simulation requirements.

Always adapt configurations to your local HPC or computing environment.

---

## Future Updates

Planned additions include:

- WRF-Chem workflows  
- Advanced urban climate experiments  
- Case study simulations over Indian cities  
- Performance optimization for HPC systems  
- Visualization templates for analysis  

---

## Contributions

Suggestions, improvements, and discussions are welcome.  
Feel free to open issues or fork this repository.

---

## Contact

https://sites.google.com/view/uvrohith
