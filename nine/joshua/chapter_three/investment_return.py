# Author: Joshua
# Title : 7% Investment return using loop 3.10

year = int(input("Enter the number of year of investment: "))
for i in range(1, year, 1):
    return_on_investment = 1000 * ((1 + 7)**i)
    print("year 1: ", i, return_on_investment)
