
# Find the pressure of the steam for a temperature of 144°C from the flowing steam table
# Temperature °C 140 150 160 170 180
# Pressure kgt/cm^2 3.685 4.84 6.302 8.076 10.225
# using Newton's forward interpolation formula.
  
# calculating u mentioned in the formula 
def u_cal(u, n):  
    temp = u; 
    for i in range(1, n): 
        temp = temp * (u - i) 
    return temp 
  
# calculating factorial of given number n 
def fact(n): 
    f = 1 
    for i in range(2, n + 1): 
        f *= i 
    return f 
  
# Number of values given 
n = 5; 
x = [ 140, 150, 160, 170, 180 ] 
      
# y[][] is used for difference table 
# with y[][0] used for input 
y = [[0 for i in range(n)] for j in range(n)] 
y[0][0] = 3.685 
y[1][0] = 4.84 
y[2][0] = 6.302 
y[3][0] = 8.076
y[4][0] = 10.225 
  
# Calculating the forward difference table 
for i in range(1, n): 
    for j in range(n - i): 
        y[j][i] = y[j + 1][i - 1] - y[j][i - 1]
  
# Displaying the forward difference table 
for i in range(n): 
    print(x[i], end = "\t")
    for j in range(n - i):
        print(y[i][j], end = "\t")
    print("")
  
# Value to interpolate at 
value = 144 
  
# initializing u and sum 
sum = y[0][0]; 
u = (value - x[0]) / (x[1] - x[0]) # r= x-x0/h
for i in range(1,n): 
    sum = sum + (u_cal(u, i) * y[0][i]) / fact(i)
  
print("\nValue at", value, "is", round(sum, 6))
  