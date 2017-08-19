from numpy import linspace,zeros

def f(t,y): 
    return  t-y

t0 = 0
tf = 1
n = 6
y0 = 1.0
t = linspace(t0,tf,n)

def euler(f,t,y0,n):
    h = (tf-t0)/(n-1)
    y = zeros([n])
    y[0] = y0
    for i in range(0,n-1):
        y[i+1] = y[i] + h*f(t[i],y[i])
    return y    

yel = euler(f,t,y0,n)

print('%9s %9s' % ('t','y'))
for i in range(n):
    print('%9.4f %9.4f' % (t[i],yel[i]))
