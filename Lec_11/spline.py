from scipy.interpolate import CubicSpline
x=[0,1,2]
y=[1,2,4]
cs=CubicSpline(x,y)
print("Using Spline : ",cs(1.5))
print("The exact answer is : ",2**1.5)
