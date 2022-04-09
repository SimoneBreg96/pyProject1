import numpy
import matplotlib

def f(x):
    if x<=1:
        return max(1,x)
    return x*f(x-1)

x = int(input("Enter a number: "))
print(f(x)) 
