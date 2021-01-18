# Write a program to solve the following system of linear equations by using Gauss-Jordan
# Elimination method.
# x + 2y + z = 8
# 2x + 3y + 4z = 20
# 4x + 3y + 2z = 16  

import numpy as np
import sys

# number of unknowns
n = 3
# numpy array of n size storing solution vector
x = np.zeros(n)

# augmented matrix coefficients
a = [[1, 2, 1, 8],
    [2, 3, 4, 20],
    [4, 3, 2, 16]]

# Applying Gauss Jordan Elimination
for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('Divide by zero detected!')
    for j in range(n):
        if i != j:
            ratio = a[j][i]/a[i][i]
            for k in range(n+1):
                a[j][k] = a[j][k] - ratio * a[i][k]


for i in range(n):
    x[i] = a[i][n]/a[i][i]

print('\nX, Y and Z is: ')
for i in range(n):
    print('X%d = %0.4f' %(i,x[i]), end = '\t')