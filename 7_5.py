from numpy import linspace,cos,sin,pi
import matplotlib.pyplot as plt

x = linspace(0,2.0*pi,40)
yc = cos(x)
ys = sin(x)
plt.plot(x,yc,'ko-',label='cos(x)')
plt.plot(x,ys,'k--',label='sin(x)')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('y = cos(x) & sin(x)')
plt.show()
