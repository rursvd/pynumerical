from numpy import array,mean,sum

# dataset 
x = array([0, 1, 2])  
y = array([1, 3, 2])
n = len(x)

xsum = sum(x)
ysum = sum(y)
xmean = mean(x)
ymean = mean(y)

xysum = 0
x2sum = 0
for i in range(n):
    xysum = xysum + x[i]*y[i]
    x2sum = x2sum + x[i]*x[i]

a = (n*xysum - xsum*ysum)/(n*x2sum - xsum**2)
b = ymean - a*xmean
print('a = ',a, 'b = ',b)
print('y = ',a,'x +',b)
