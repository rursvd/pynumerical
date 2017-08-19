
def f(x):
    return x**3 -2.0*x**2 + 3*x -1.0 

# 2nd order differentiation 
def ddiff(f,x,h):
    diff = (f(x+h) - 2.0*f(x) + f(x-h))/h**2
    return diff 

h = 0.25
x = 0.5
diff = ddiff(f,x,h)

print('dfdx2 = %8.4f' % diff)
