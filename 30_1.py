from numpy import array

x = array([1,2,3,4,5])
fx = array([1,4,9,16,25])

n = len(x)-1
h = (x[n]-x[0])/n

trap = 0.0
for i in range(1,n):
    trap = trap + fx[i]

trap = h*(fx[0] + 2.0* trap + fx[n])/2.0    
print('T = %8.4f' % trap)
