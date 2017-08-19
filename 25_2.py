from numpy import array,zeros

def linearintp(x0,x1,f0,f1):
    a1= (f1-f0)/(x1-x0)
    a0 = f0 
    return a0, a1
    
# dataset 
x = array([0, 1, 2])
y = array([1, 3, 2])

n = len(x)
for i in range(n-1):
    x0 = x[i]
    x1 = x[i+1]
    f0 = y[i]
    f1 = y[i+1]
    a0, a1 = linearintp(x0,x1,f0,f1)
    print('f(x) = ',a0,'+',a1,'(x - ',x0,')')
