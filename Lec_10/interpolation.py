
def interpolate(x,x1,y1,x2,y2,x3,y3):
    a=(x-x2)*(x-x3)*y1/((x1-x2)*(x1-x3))
    b=(x-x1)*(x-x3)*y2/((x2-x1)*(x2-x3))
    c=(x-x1)*(x-x2)*y3/((x3-x1)*(x3-x2))
    return a+b+c
def exact(x):
    return 2**x
print("The interpolation gives for x=1.5 the result ",interpolate(1.5,0,1,1,2,2,4))
print("The exact result is ", exact(1.5))
