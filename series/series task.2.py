import math

x = float(input())
def taylor(x):
    series = 0
    for n in range (16):
        a = ((-1)**n)*(x**(2*n))/(math.factorial(2*n))
        series = series + a
    return series
                                  
print (taylor(x))
