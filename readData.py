import netCDF4 as nc
import pandas as pd
import numpy as np

# Open the NetCDF file
ds = nc.Dataset('IonianTemperature.nc', 'r')  # Replace 'path_to_your_file.nc' with the actual file path

print



# Initialize a dictionary to hold data
# List all variables
# print("Variables in the file:")
# for var in ds.variables:
#     print(var, ds.variables[var])






# Variables:

# 1st
# find given density at depth using equation

# Validate This:
# P = P_0 + ρgh // pressure, P_0 in hPa
def findPressure(depth):
    P_0 = 1013.25
    density = 1025 # can slightly vary (kg/m^3)
    g = 9.81 # m/s^2
    h = depth # m
    return P_0 + density*g*h

# def findDensity(lat,long,depth):
#     pressure = findPressure(depth)
#     temp = 
#     salinity = 

# 2nd
# find given velocity at depth using data

# 3rd
# Factor EZ rising speed, then slow, then with provisions
# choice of complexity and accuracy

# 4th
# Model Path using constant (then decaying speeds)
# Path: { Buoyancy, Drag, || Vectors}

# 5th, Simulations
# Error
# Carribbean Case Study?
# Cases
# Error Definition and Generalization
# Finally Visualization



# Close the dataset
ds.close()
