from numpy import linspace, zeros

def f(x):
    return -x**2 + 6.0*x -5.0

def df(x):
    return -2.0*x + 6.0

n = 7
x = zeros(n)
x[0] = -2.0

for k in range(n-1):
    x[k+1] = x[k] - f(x[k])/df(x[k])
    
# printing output
print("%5s %8s" % ('k','x'))
for k in range(n):
    print("%5d %9.4f" % (k+1,x[k]))
