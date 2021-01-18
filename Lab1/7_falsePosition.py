
# Write a program to find the root of the equation x^3 + x – 1 = 0, correct to 3 decimal places, by using
# false position method.

def f(x):
    return x**3 + x - 1

# Implementing False Position Method
def falsePosition(x0,x1,e):
    step = 1
    print('\n\n FALSE POSITION METHOD IMPLEMENTATION ')
    condition = True
    while condition:
        x2 = x0 - (x1-x0) * f(x0)/( f(x1) - f(x0) )
        print('Iteration-> %d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2

        step = step + 1
        condition = abs(f(x2)) > e

    print('\nRequired root is: %0.3f' % x2)

x0 = float(input('First Guess: '))
x1 = float(input('Second Guess: '))
e = float(input('Tolerable Error: '))


# Checking Correctness of initial guess values and false positioning
if f(x0) * f(x1) > 0.0:
    print('Given guess values do not bracket the root.')
    print('Try Again with different guess values.')
else:
    falsePosition(x0,x1,e)