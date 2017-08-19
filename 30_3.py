from numpy import array

x = array([1,2,4,7,8])
fx = array([1,4,16,49,64])

n = len(x)-1

trap = 0.0
for i in range(0,n):
    h = x[i+1] - x[i]
    trap = trap + h*(fx[i+1]+fx[i])/2.0
   
print('T = %8.4f' % trap)
