import numpy as np
def f(x):
    return (10-x**2);
n=int(input("Enter the no of intervals: "))
x=np.linspace(-2,2,n)
result=0
h1=4/(n-1)
h2=2/(n-1)
for i in range (0,n):
    if(i==0):
        result=result+h2*f(x[i])
    if(i==n-1):
        result=result+h2*f(x[i])
    else:
        result=result+h1*f(x[i])

print("The result of the integration is : ",result)
    
