from numpy import exp,sqrt

def f(x):
    return x**2*exp(-x)/sqrt(1.0 + x**2)

def trapezoidal(f,a,b,n):
    h = (b-a)/n
    trap = 0.0
    for i in range(1,n):
        x = a + i*h
        trap = trap + 2.0*f(x) 
    trap = h*(f(a) + trap + f(b))/2.0
    return trap

T = trapezoidal(f,-1,1,2)
print('T = %8.4f' % T) 
