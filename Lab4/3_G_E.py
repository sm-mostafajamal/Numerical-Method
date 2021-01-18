# Write a program to solve the following system of linear equations by using Gaussian
# Elimination method.
# 2x + y + z = 10
# x + 4y + 9z = 16
# 3x + 2y + 3z = 18

import numpy as np
import sys

# number of unknowns
n = 3
# numpy array of n size storing solution vector
x = np.zeros(n)

# augmented matrix coefficients
a = [[2, 1, 1, 10],
    [1, 4, 9, 16],
    [3, 2, 3, 18]]

# Applying Gauss Elimination
for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('Divide by zero detected!')   
    for j in range(i+1, n):
        ratio = a[j][i]/a[i][i]
        for k in range(n+1):
            a[j][k] = a[j][k] - ratio * a[i][k]

# Back Substitution
x[n-1] = a[n-1][n]/a[n-1][n-1]
for i in range(n-2,-1,-1):
    x[i] = a[i][n]
    for j in range(i+1,n):
        x[i] = x[i] - a[i][j]*x[j]
    
    x[i] = x[i]/a[i][i]


print('\nX, Y and Z is: ')
for i in range(n):
    print('X%d = %0.4f' %(i,x[i]), end = '\t')