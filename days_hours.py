"""
----------------------------------------------------------
Name:    days_hours.py
Purpose: Converting the numbers of hours to days and hours.

Author:  Hosey.K

Created: date in 08/02/2021
----------------------------------------------------------
"""

print("Hours to Days and Hours Converter")

# Get the number of  hours
hours = int(input("Enter the number of hours: "))

# Calculate for days and hours
days = hours//24
num_days = str(round(days))

d_hours = hours%24

# Output results
print(hours,"is",days,"days and",d_hours,"hours.")

