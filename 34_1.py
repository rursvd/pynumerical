from numpy import linspace,zeros

def f(t,y): 
    return  t-y

t0 = 0
tf = 1
n = 6
y0 = 1.0
t = linspace(t0,tf,n)

def rk2(f,t,y0,n):
    h = (tf-t0)/(n-1)
    y = zeros([n])
    y[0] = y0
    for i in range(0,n-1):
        K0 = f(t[i], y[i])
        K1 = f(t[i] + 3.0/4.0*h, y[i] + 3.0/4.0*h*K0)
        y[i+1] = y[i] + h/3.0*(K0 + 2.0*K1)
    return y

yrk2 = rk2(f,t,y0,n)

# printing output
print('%9s %9s' % ('t', 'y'))
for i in range(n):
    print('%8.4f %8.4f' % (t[i],yrk2[i]))
