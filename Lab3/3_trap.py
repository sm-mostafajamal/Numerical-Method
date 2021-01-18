# SOLVE - 03
# Write a program to calculate the approximate area under the curve y = ∫ 5 log 10 x dx
# by using trapezoidal rule. [lower limit 1]

import math
def f( x ):  
    # f(x) = log10 x 
    return (math.log10(x)) 
      
# implementing trapezoidal rule
def trapezoidal (a, b, n): 
    # calculating step size
    h = (b - a) / n 
      
    # Computing sum of first(y0) and last terms(y1) 
    sum = (f(a) + f(b)) 
    # Adding middle terms in above formula 
    for i in range(1,n):
        sum += 2 * f(a + i * h) # x = a + ih
    # Finding final integration value
    return ((h / 2) * sum) 
  
# Range of definite integral 
a = 1
b = 5
n = 6

print ("Integration result by Trapeziodal method is: ", trapezoidal(a, b, n)) 
  