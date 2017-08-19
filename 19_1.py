from numpy import zeros
import matplotlib.pyplot as plt

m = 8
x1 = zeros(m)
x2 = zeros(m)
x3 = zeros(m)
print('%7s %9s %9s %9s' % ('k','x1','x2','x3'))
print('%7d %9.5f %9.5f %9.5f' % (0,x1[0],x2[0],x3[0]))

for k in range(m-1):
    x1[k+1] = (-1.0 + 2.0*x2[k] - 3.0*x3[k])/5.0
    x2[k+1] = (2.0 + 3.0*x1[k+1] - x3[k])/9.0
    x3[k+1] = (-3.0 + 2.0*x1[k+1] - x2[k+1])/7.0
    print('%7d %9.5f %9.5f %9.5f' % (k+1,x1[k+1],x2[k+1],x3[k+1]))

