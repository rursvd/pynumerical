from numpy import array,mean,sum,log,exp,linspace

def f(a,b,x):
    return b*exp(a*x)

# dataset 
x = array([0, 1, 2, 4])  
yo = array([2, 4, 8, 15])

y = log(yo)
n = len(x)

xsum = sum(x)
ysum = sum(y)
xmean = mean(x)
ymean = mean(y)
xysum = sum(x*y)
x2sum = sum(x**2)

A = (n*xysum - xsum*ysum)/(n*x2sum - xsum**2)
B = ymean - A*xmean
print('A = %8.4f B = %8.4f' % (A, B))
b = exp(B)
a = A
print('a = %8.4f b = %8.4f' % (a,b))
