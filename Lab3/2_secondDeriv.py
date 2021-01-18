# SOLVE - 02
# The following values of f (x) are given.
# x 1 2 3 4 5
# y = f(x) 1 8 27 64 125
# Write a program to find difference table for the above values.

  
# Number of values given
value = 1.5 
n = 5; 
x = [ 1, 2, 3, 4, 5 ] 
      
# y[][] is used for difference table 
# with y[][0] used for input 
y = [[0 for i in range(n)] for j in range(n)] 
y[0][0] = 1
y[1][0] = 8
y[2][0] = 27 
y[3][0] = 64
y[4][0] = 125

  
# (del) Calculating the forward difference table 
for i in range(1, n): 
    for j in range(n - i): 
        y[j][i] = y[j + 1][i - 1] - y[j][i - 1]

# Displaying the forward difference table 
for i in range(n): 
    print(x[i], end = "\t")
    for j in range(n - i): 
        print(y[i][j], end = "\t")
    print("")


h =  (x[1] - x[0])
u = (value - x[0]) / h 

# factorial
def fact(n): 
    f = 1 
    for i in range(2, n + 1): 
        f *= i 
    return f 

sum = 0 
# For first derivative
for i in range(1,n):
    if i == 1:
        sum += (y[0][i]/fact(i))
    elif i == 2: 
        sum += (2*u-1)*y[0][i] / fact(i)
    elif i == 3:
        sum += (3*u**2-6*u+2)*y[0][i]/fact(i)
    sum = sum / h
    
print("\nFirst derivative: ", sum)

# For second derivative
sum2 = 0
for i in range(2,n): 
    if i == 2:
        sum2 += (y[0][i])
    elif i == 3: 
        sum2 += (u-1)*y[0][i]
    elif i == 4:
        sum2 += ((6*u**2-18*u+11)/12)*y[0][i]   

    sum2 = sum2 / h**2
print("\nSecond derivative: ", sum2)



