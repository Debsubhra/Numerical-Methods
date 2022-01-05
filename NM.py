def f(x):
    return (x**2-10)
def fprime(x):
    return (2*x)

x_0=0.2
for i in range (0,100):
    x_0=x_0-f(x_0)/fprime(x_0)
print("The positive root is ",x_0)
x_0=-0.1
for j in range (0,100):
    x_0=x_0-f(x_0)/fprime(x_0)
print("The negative root is ",x_0)
