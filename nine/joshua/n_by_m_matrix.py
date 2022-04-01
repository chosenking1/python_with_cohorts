# Author: Joshua
# Title : checking if matrix is similar diagonally.
import numpy as np

n = int(input("Enter the number of rows:"))
m = int(input("Enter the number of columns:"))

checker = []

# Initialize matrix
matrix = []
print("Enter the entries row-wise:")

# For user input
for i in range(n):  # A for loop for row entries
    a = []
    for j in range(m):  # A for loop for column entries
        a.append(int(input()))
    matrix.append(a)

# For printing the matrix
# for i in range(n):
#     for j in range(m):
#         print(matrix[i][j], end=" ")
#     print()
# if m == 1 or n == 1:
#     print(1)
count = 0
for i in range(n - 1):
    count = count + 1
    for j in range(m - 1):

        if matrix[i][j] == matrix[i + 1][j + 1]:
            # print(matrix[i][j], " ", matrix[i + 1][j + 1], i, j)
            checker.append(1)

        else:

            # print(matrix[i][j], " ", matrix[i + 1][j + 1], i, j)
            checker.append(0)


if checker.__contains__(0):
    print(0)
else:
    print(1)
