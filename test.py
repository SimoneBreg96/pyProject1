import numpy
import matplotlib

def factorial(x):
    if x<=1:
        return max(1,x)
    return x*factorial(x-1)

def newFunction(n):
    if(n<=2):
        return [1,2]
    t_prev = 1
    t = 2
    while(t<n):
        temp = t
        t = t+t_prev
        t_prev = temp
    return [t_prev,t]

x = int(input("Enter a number: "))
print("factorial:",factorial(x)) 
print("Fibonacci previous, present and following number:", newFunction(x))