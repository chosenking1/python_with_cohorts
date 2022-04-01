# Author: Joshua
# Title :3.11


# Enter the gallons used (-1 to end): 12.8
# Enter the miles driven: 287
# The miles/gallon for this tank was 22.421875
# Enter the gallons used (-1 to end): 10.3
# Enter the miles driven: 200
# The miles/gallon for this tank was 19.417475
# Enter the gallons used (-1 to end): 5
# Enter the miles driven: 120
# The miles/gallon for this tank was 24.000000
# Enter the gallons used (-1 to end): -1
# The overall average miles/gallon was 21.601423

gallons = 0
total_miles = 0
total_gallons = 0
miles_driven = 0

while miles_driven != -1:
    miles_driven = float(input("Type in the millage"))
    gallons = float(input("Type in the Gallon"))
    average = miles_driven / gallons
    print("The miles/gallon for this tank was ", average)
    total_miles += miles_driven
    total_gallons += gallons

print("The overall ", total_miles / total_gallons)

miles_driven = miles_driven
