
# Find the population of a town in 2006, with the help of the following data
# year 1961 1971 1981 1991 2001 2011
# population 20 27 39 52 70 90
# (in millions)
# using Newton's backward interpolation formula.
  
# calculating u mentioned in the formula 
def u_cal(u, n):  
    temp = u
    for i in range(1, n): 
        temp = temp * (u + i)
    return temp
  
# calculating factorial of given number n 
def fact(n): 
    f = 1
    for i in range(2, n + 1): 
        f *= i
    return f
  
# Number of values given 
n = 5; 
x = [ 1961, 1971, 1981, 1991, 2001  ]
      
# y[][] is used for difference table 
# with y[][0] used for input 
y = [[0 for i in range(n)] for j in range(n)] 
y[0][0] = 20
y[1][0] = 27 
y[2][0] = 39 
y[3][0] = 52
y[4][0] = 70 
  
# Calculating the forward difference table 
for i in range(1, n): 
    for j in range (n-1,i-2,-1): 
        y[j][i] = y[j][i - 1] - y[j - 1][i - 1]
  
# Displaying the forward difference table 
for i in range(0,n): 
    print(x[i], end = "\t")
    for j in range(0,i+1): 
        print(y[i][j], end = "\t")
    print("")

# Value to interpolate at 
value = 2006
  
# initializing u and sum 
sum = y[n - 1][0]
u = (value - x[n - 1]) / (x[1] - x[0])
for i in range(1,n): 
    sum = sum + (u_cal(u, i) * y[n - 1][i]) / fact(i)
  
print("\nValue at", value, "is", round(sum, 6))
  