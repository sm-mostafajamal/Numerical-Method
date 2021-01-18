
# SOLVE - 04
# Write a program to calculate the approximate area under the curve y = ∫ pi/2 e^sinx dx by using
# Simpson’s 1/3 rule. [lower limit 0]
import math
def f(x):
    # f(x) = e^sin(x)
    return math.exp(math.sin(x))

# Implementing Simpson's 1/3 
def simpson13(a, b, n):
    # calculating step size
    h = (b - a) / n
    
    # Computing sum of first(y0) and last terms(y1) 
    sum = f(a) + f(b)
    # Adding other terms in above formula 
    for i in range(1,n):
        if i%2 == 0:
            sum += 2 * f(a + i * h)
        else:
            sum += + 4 * f(a + i * h)
    # Finding final integration value
    return sum * h/3
    
# Range of definite integral 
a = 0
b = math.pi/2
n = 6

print("Integration result by Simpson's 1/3 method is: ", simpson13(a, b, n) )
