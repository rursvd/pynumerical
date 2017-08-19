from numpy import linspace,zeros

def f(t,y): 
    return  t-y

t0 = 0
tf = 1
n = 6
y0 = 1.0
t = linspace(t0,tf,n)

def ab2(f,t,y0,n):
    h = (tf-t0)/(n-1)
    y = zeros(n)
    y[0] = y0
    y[1] = y[0] + h*f(t[0],y[0])
    for i in range(1,n-1):
        y[i+1] = y[i] + (3.0/2.0)*h*f(t[i],y[i])-1.0/2.0*h*f(t[i-1],y[i-1])
    return y

yab2 = ab2(f,t,y0,n)

print("%5s %8s" % ('t','y'))
for i in range(0,n):
    print("%5.1f %9.4f" % (t[i],yab2[i]))
