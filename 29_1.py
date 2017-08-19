from numpy import exp,sqrt

def f(x):
    return x**2*exp(-x)/sqrt(1.0 + x**2)

def simpson(f,a,b,n):
    h = (b-a)/n
    simp = 0.0
    for i in range(1,n):
        x = a + i*h
        if (i%2 == 1):
            simp = simp + 4.0*f(x)
        else:    
            simp = simp + 2.0*f(x)
    simp = h*(f(a) + simp + f(b))/3.0
    return simp

T = simpson(f,-1,1,4)
print('T = %8.4f' % T)
