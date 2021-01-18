# Write a program to solve the following system of linear equations by using Gauss-Seidel
# method.
# 10x + y + z = 12
# 2x + 10y + z = 13
# 2x + 2y + 10z = 14

# diagonally dominant form
f1 = lambda x,y,z: (12-y-z)/10
f2 = lambda x,y,z: (13-2*x-z)/10
f3 = lambda x,y,z: (14-2*x-2*y)/10


# guassing
x0 = 0
y0 = 0
z0 = 0
count = 1

e = float(input('Enter tolerable error: '))# ager iteration and current tar error diff kotho hole print korbe

# Implementation of Gauss Seidel Iteration
print('\nCount\tx\ty\tz\n')

condition = True

while condition:
    x1 = f1(x0,y0,z0)
    y1 = f2(x1,y0,z0)
    z1 = f3(x1,y1,z0)
    print('%d\t%0.4f\t%0.4f\t%0.4f\n' %(count, x1,y1,z1))
    e1 = abs(x0-x1);
    e2 = abs(y0-y1);
    e3 = abs(z0-z1);
    
    count += 1
    x0 = x1
    y0 = y1
    z0 = z1
    
    condition = e1>e and e2>e and e3>e

print('\nSolution: x = %0.3f, y = %0.3f and z = %0.3f\n'% (x1,y1,z1))
