import numpy

def factorial(x):
    if x<=1:
        return max(1,x)
    return x*factorial(x-1)

x = int(input("Enter a number: "))
print(factorial(x)) 