def f(x):
    return 10-3*x**2
a=-1
b=3
n=4
h=(b-a)/n
integral=h*(f(a)+f(b)+4*f(a+h)+2*f(a+2*h)+4*f(a+3*h))/3
print("The value of the integral is : ", integral)
