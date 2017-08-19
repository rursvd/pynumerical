from numpy import linspace, zeros, sign, cos

def f(x):
    return -x**2 + 6.0*x -5.0

a = -2.0
b = 3.0
n = 7
c = zeros(n)

for i in range(n):
    c[i] = (a + b)/2.0
    if sign(f(c[i])) == sign(f(a)):
        a = c[i]
    else:
        b = c[i]   

# printing output
print("%5s %8s" % ('k','c'))
for k in range(n):
    print("%5d %9.4f" % (k+1,c[k]))

