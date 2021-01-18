# Given an equation: f(x) = p*e-x + q*sin(x) + r*cos(x) + s*tan(x) + t*x2 + u = 0 and the values for p,q,r,s,t,u.
# Find the value for x (if exists), where 0 <= x <= 1.
from math import (exp, sin, cos, tan)

p, q, r, s, t, u= [float(i) for i in input("Enter six value(p,q,r,s,t,u): ").split()]

def eval(x):
  return p * exp(-x) + q * sin(x) + r * cos(x) + s * tan(x) + t * x**2 + u

def main():
    low = 0.0
    mid = 0.5 
    high = 1.0
    while(high - low > 0.0000001):
      mid = (low + high) / 2.0
      emid = eval(mid) 
      ehigh = eval(high)
      if (ehigh < 0 and emid > 0) or  (ehigh >= 0 and emid > ehigh) or  (ehigh <= 0 and ehigh > emid):
        low = mid
      else:
        high = mid

    if(abs(emid) <= 0.0001):
      print("{:.4f}\n".format(mid))
    else:
      print("No solution\n");

if __name__ == '__main__':
  main()