# Author: Joshua
# Title : 3.12
number = int(input("Type an integer"))
num1 = number
for i in range(5):
    base_number = 10**i

    first = num1 // base_number
    num1 = num1 % base_number

    print(first, "", end="")




