from numpy import linspace,zeros

def f(t,y): 
    return  t-y

t0 = 0
tf = 1
n = 6
y0 = 1.0
t = linspace(t0,tf,n)

def rk4(f,t,y0,n):
    h = (tf-t0)/(n-1)
    y = zeros([n])
    y[0] = y0
    for i in range(0,n-1):
        K0 = f(t[i], y[i])
        K1 = f(t[i] + h/2.0, y[i] + h/2.0 * K0 )
        K2 = f(t[i] + h/2.0, y[i] + h/2.0 * K1 )
        K3 = f(t[i] + h, y[i] + h * K2)
        y[i+1] = y[i] + h/6.0 * (K0 + 2.0*K1 + 2.0*K2 + K3)
    return y

yrk4 = rk4(f,t,y0,n)

# printing output
print('%8s %8s' % ('t','y'))
for i in range(n):
    print('%9.4f %9.4f' % (t[i],yrk4[i]))
