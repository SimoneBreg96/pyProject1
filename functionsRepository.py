import numpy
import matplotlib

def factorial(x):
    if x<=1:
        return max(1,x)
    return x*factorial(x-1)

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def fibonacci(n):
    if(n<=2):
        return [1,2]
    t_prev = 1
    t = 2
    while(t<n):
        temp = t
        t = t+t_prev
        t_prev = temp
    return [t_prev,t]

def fuelPrice(d,p,c):
    if(c==0):
        return 0
    return d*p/c



# x = int(input("Enter a number: "))
# print("factorial:",factorial(x)) 
# print("Fibonacci previous, present and following number:", fibonacci(x))