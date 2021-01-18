# Write a program to solve the following system of linear equations by using Jacobi's method.
# 83x + 11y - 4z = 95
# 3x + 8y + 29z = 71
# 7x + 52y + 13z = 104
#         or,
# 83x + 11y - 4z = 95
# 7x + 52y + 13z = 104
# 3x + 8y + 29z = 71

# changing the equation and diagonally dominant form
f1 = lambda x,y,z: (95 - 11*y + 4*z) /83
f2 = lambda x,y,z: (104 - 7*x - 13*z) /52
f3 = lambda x,y,z: (71 - 3*x - 8*y) /29

# guassing
x0 = 0
y0 = 0
z0 = 0
count = 1

e = float(input('Enter tolerable error: ')) # ager iteration and current tar error diff kotho hole print korbe

# Implementation of Jacobi Iteration
print('\nCount\tx\ty\tz\n')

condition = True

while condition:
    x1 = f1(x0,y0,z0)
    y1 = f2(x0,y0,z0)
    z1 = f3(x0,y0,z0)
    print('%d\t%0.4f\t%0.4f\t%0.4f\n' %(count, x1,y1,z1))
    e1 = abs(x0-x1);
    e2 = abs(y0-y1);
    e3 = abs(z0-z1);
    
    count += 1
    x0 = x1
    y0 = y1
    z0 = z1
    
    condition = e1>e and e2>e and e3>e

print('\nSolution: x = %0.4f, y = %0.4f and z = %0.4f\n'% (x1, y1, z1))