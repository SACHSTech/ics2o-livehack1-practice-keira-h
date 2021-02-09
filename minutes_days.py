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
days = minutes//(60*24)
num_days = str(round(days))

hours = (minutes%(24*60))//60

mins = (minutes%(24*60))%60

# Output results
print(minutes,"is",days,"days,",hours,"hours, and",mins,"minutes.")