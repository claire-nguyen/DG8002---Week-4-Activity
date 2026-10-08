# Complete the TODOs using the Python concepts introduced in class.
# Run this file to check your result.  

# DG8002 - F26 - Activity 4
# Author Name: Claire Nguyen
# Date: 06 Oct 2026

# SCENARIO
# A weather station has recorded temperatures over seven days. 
# Your task is to examine the data and produce a short weather report.

#                 M   T   W  Th  F   Sa  Su
temperatures  = [18, 22, 25, 19, 27, 24, 16]

# TODO 0: Create the variables you need for total temperature, # of days above 23 degrees, and hottest day
# TODO 1: Iterate through every recorded temperature
    # TODO 2: Print the recorded temperature
    # TODO 3: Add the temperature to total
    # TODO 4: If temperature is above 23, add 1 to the day counter
# TODO 5: Calculate and print the average temeprature for the week.
# TODO 6: Print how many days exceeded 23 degrees
# TODO 7: Print the -> index <- of the highest temperature.

total_temperature = 0
days_above23 = 0
hottest_day = -1

for index in temperatures:
    print(f"Recorded Temperature: {index}")
    total_temperature += index
    if index > 23:
        days_above23 += 1
    if index == max(temperatures):
        hottest_day = temperatures.index(index)
print (f"Average Temperature: {total_temperature / len(temperatures):.2f}")
print (f"Days Above 23: {days_above23}")
print (f"Highest Temperature Index: {hottest_day}")

# EXPECTED OUTPUT
# Average Temperature: 21.57
# Days Above 23:  3
# Highest Temperature Index: 4  


