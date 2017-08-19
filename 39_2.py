from numpy import linspace,zeros

def g(t,y,v):
    return 1.0 + v - y**2 - v**2

def f(t,y,v):
    return 1.0 - y - y**2 - v**2

t0 = 0
tf = 4
n = 6
y0 = 0.0
v0 = 1.0
t = linspace(t0,tf,n)

def rk4_set(g,f,t,y0,v0,n):
    h = (tf-t0)/(n-1)
    y = zeros(n)
    v = zeros(n)
    y[0] = y0
    v[0] = v0
    for i in range(0,n-1):
        K0 = g(t[i],y[i],v[i])
        L0 = f(t[i],y[i],v[i])
        K1 = g(t[i] + h/2.0, y[i] + h/2.0 * K0, v[i] + h/2.0 * L0)
        L1 = f(t[i] + h/2.0, y[i] + h/2.0 * K0, v[i] + h/2.0 * L0)
        K2 = g(t[i] + h/2.0, y[i] + h/2.0 * K1, v[i] + h/2.0 * L1)
        L2 = f(t[i] + h/2.0, y[i] + h/2.0 * K1, v[i] + h/2.0 * L1)
        K3 = g(t[i] + h, y[i] + h * K2, v[i] + h * L2)
        L3 = f(t[i] + h, y[i] + h * K2, v[i] + h * L2)
        y[i+1] = y[i] + h/6.0 * (K0 + 2.0*K1 + 2.0*K2 + K3)
        v[i+1] = v[i] + h/6.0 * (L0 + 2.0*L1 + 2.0*L2 + L3)
    return y,v
   

y, v = rk4_set(g,f,t,y0,v0,n)

print('%5s %8s %8s' % ('t','y','v')) 
for i in range(0,n):
    print("%5.1f %9.4f %9.4f" % (t[i],y[i],v[i]))
