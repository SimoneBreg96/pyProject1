import numpy

def f(x):
    if x<=1:
        return max(1,x)
    return x*f(x-1)

print(f(10))
