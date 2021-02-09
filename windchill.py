"""
----------------------------------------------------------
Name:    windchill.py
Purpose: Compute the windchill factor from the temperature in celsius and wind speed in km/h.  

Author:  Hosey.K

Created: date in 08/02/2021
----------------------------------------------------------
"""

# Get the temperature and wind speed
temperature = float(input("Enter the temperature (°C): "))
wind_spd = float(input("Enter the wind speed (km/h): "))

# Define variables
T = temperature
V = wind_spd

# Calculate the wind chill factor
WCF = 13.12+(0.6215*float(T))-(11.37*float(V)**0.16)+ (0.3965*float(T)*float(V)**0.16)
wind_chill = str(round(WCF, 2))

# Output results
print("When the temperature is",temperature,"°C, wind speed is",wind_spd,"km/h, the wind chill is",wind_chill,"°C.")

