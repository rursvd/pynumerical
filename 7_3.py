from numpy import linspace,cos,pi
import matplotlib.pyplot as plt

x = linspace(0,2.0*pi,40)
y = cos(x)
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('y = cos(x)')
plt.show()
