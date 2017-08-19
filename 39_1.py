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

def euler_set(g,f,t,y0,v0,n):
    h = (tf-t0)/(n-1)
    y = zeros(n)
    v = zeros(n)
    y[0] = y0
    v[0] = v0
    for i in range(0,n-1):
        y[i+1] = y[i] + h*g(t[i],y[i],v[i])
        v[i+1] = v[i] + h*f(t[i],y[i],v[i])
    return y,v    

y, v = euler_set(g,f,t,y0,v0,n)

print('%5s %8s %8s' % ('t','y','v')) 
for i in range(0,n):
    print("%5.1f %9.4f %9.4f" % (t[i],y[i],v[i]))
