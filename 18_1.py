from numpy import zeros	  
import matplotlib.pyplot as plt

m = 8 
x1j = zeros(m)
x2j = zeros(m)
x3j = zeros(m)
print('%7s %9s %9s %9s' % ('k','x1','x2','x3'))
print('%7d %9.5f %9.5f %9.5f' % (0,x1j[0],x2j[0],x3j[0]))

for k in range(m-1):
    x1j[k+1] = (-1.0 + 2.0*x2j[k] - 3.0*x3j[k])/5.0
    x2j[k+1] = (2.0 + 3.0*x1j[k] - x3j[k])/9.0
    x3j[k+1] = (-3.0 + 2.0*x1j[k] - x2j[k])/7.0
    print('%7d %9.5f %9.5f %9.5f' % (k+1,x1j[k+1],x2j[k+1],x3j[k+1])) 

