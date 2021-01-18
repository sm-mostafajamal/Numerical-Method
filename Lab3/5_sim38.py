
# SOLVE - 05
# Write a program to calculate the approximate area under the curve y = ∫1 x / (1+x)
# by using Simpson’s 3/8 rule. [lower limit 0]

def f(x): 
    # f(x) = x/(1+x)
    return (x / (1 + x)) 
   
# Implementing Simpson's 3/8 
def simpson38(a, b, n): 
    # calculating step size
    h = (float(b - a) / n) 

    # Computing sum of first(y0) and last terms(y1) 
    sum = f(a) + f(b) 
    # Adding other terms in above formula 
    for i in range(1, n ): 
        if (i % 3 == 0): 
            sum = sum + 2 * f(a + i * h) 
        else: 
            sum = sum + 3 * f(a + i * h) 
    # Finding final integration value
    return ((float( 3 * h) / 8 ) * sum ) 
  
# Range of definite integral 
a = 0
b = 1
n = 6

print ("Integration result by Simpson's 3/8 method is: ",simpson38(a, b, n) ) 
  