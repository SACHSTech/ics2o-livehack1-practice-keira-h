"""
----------------------------------------------------------
Name:    minutes_days.py
Purpose: Converting the number of minutes to number of days,hours and minutes.

Author:  Hosey.K

Created: date in 08/02/2021
----------------------------------------------------------
"""

# Get the numbers of minutes
minutes = int(input("Enter the number of minutes: "))

# Calculate for days, hours and minutes
mins_in_days = 60*24
days = minutes//mins_in_days
num_days = str(round(days))

hours = 60//24

mins = minutes%24

# Output results
print(minutes,"is",days,"days,",hours,"hours, and",mins,"minutes.")