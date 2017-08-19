from numpy import linspace,zeros,exp
import matplotlib.pyplot as plt

def f(t,y): 
    return  t-y

def exact(t):
    return t-1.0+2.0*exp(-t)

t0 = 0
tf = 1
n = 6
y0 = 1.0

t = linspace(t0,tf,n)

def abm4(f,t,y0,n):
    h = (tf-t0)/(n-1)
    y = zeros([n])
    y[0] = y0
    for i in range(0,3):
        K0 = f(t[i], y[i])
        K1 = f(t[i] + h/2.0, y[i] + h/2.0 * K0 )
        K2 = f(t[i] + h/2.0, y[i] + h/2.0 * K1 )
        K3 = f(t[i] + h, y[i] + h * K2)
        y[i+1] = y[i] + h/6.0 * (K0 + 2.0*K1 + 2.0*K2 + K3)
    
    for i in range(3,n-1):
        yp = y[i] + h/24.0*(55.0*f(t[i],y[i])-59.0*f(t[i-1],y[i-1])+37.0*f(t[i-2],y[i-2]) 
                                                  -9.0*f(t[i-3],y[i-3]))
        y[i+1] = y[i] + h/24.0*(9.0*f(t[i+1],yp) +19.0*f(t[i],y[i]) -5.0*f(t[i-1],y[i-1])
                               + f(t[i-2],y[i-2]))
    return y

yabm4 = abm4(f,t,y0,n)

print("%5s %8s" % ('t','y'))
for i in range(0,n):
    print("%5.1f %9.4f" % (t[i],yabm4[i]))
