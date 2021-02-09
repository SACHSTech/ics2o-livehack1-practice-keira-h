"""
----------------------------------------------------------
Name:    f_to_c.py
Purpose: Change the degree measure in fahrenheit to celsius

Author:  Hosey.K

Created: date in 08/02/2021
----------------------------------------------------------
"""

print("------------ Fahrenheit to Celsius Converter ------------")

# Get the temperature
fahrenheit = float(input("Enter the value in Fahrenheit (°F): "))

# Calculate for celsius
celsius = (float(fahrenheit) - 32) * 5.00/9.00

# Output results
number = str(round(celsius, 2))
print(fahrenheit, "in celsius is",number,"°C.")

