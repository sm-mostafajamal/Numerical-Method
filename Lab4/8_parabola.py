# Write a program to find the least square parabola y = a + bx + cx 2 for the following data
# x -3 -1 1 3
# y 15 5 1 5


x = [1, 2, 3, 4]
y = [6, 11, 18, 27]
sx = sum(x)
sy = sum(y)
n = len(x)
sxsy = 0
sx2 = 0
sx3 = 0
sx4 = 0
sx2y = 0
for i in range(n):
    sxsy += x[i] * y[i]
    sx2 += x[i] ** 2
    sx3 += x[i] ** 3
    sx4 += x[i] ** 4
    sx2y += x[i] ** 2 * y[i]


print('%.2f'%n,'*a0','+','%.2f'%sx,'*a1','+','%.2f'%sx2,'*a2','=','%.2f'%sy)
print('%.2f'%sx,'*a0','+','%.2f'%sx2,'*a1''+','%.2f'%sx3,'*a2','=','%.2f'%sxsy)
print('%.2f'%sx2,'*a0','+','%.2f'%sx3,'*a1','+','%.2f'%sx4,'*a2','=','%.2f'%sx2y)


# diagonally dominant form
f1 = lambda x,y,z: (62-10*y-30*z)/4
f2 = lambda x,y,z: (190-10*x-100*z)/30
f3 = lambda x,y,z: (644-30*x-100*y)/354


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

print('\nSolution: a0 = %0.3f, a1 = %0.3f and a2 = %0.3f\n'% (x1,y1,z1))





