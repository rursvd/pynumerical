from numpy import linspace,zeros

def f(t,y): 
    return  t-y

t0 = 0
tf = 1
n = 6
y0 = 1.0
t = linspace(t0,tf,n)
 
def heun(f,t,y0,n):
    h = (tf-t0)/(n-1)
    y = zeros(n)
    y[0] = y0
    for i in range(0,n-1):
        yp = y[i] + h*f(t[i],y[i])
        y[i+1] = y[i] + h/2.0 * (f(t[i],y[i]) + f(t[i+1],yp))
    return y  

yhe = heun(f,t,y0,n)

# printing output
print('%8s %8s' % ('t','y'))
for i in range(n):
    print('%9.4f %9.4f' % (t[i],yhe[i]))
