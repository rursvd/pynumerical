from numpy import array,zeros,linspace,copy
from numpy.linalg import det

def cramer(a,b):
    n = len(b)
    xs = zeros(n)
    for i in range(n):
        cram = copy(a)
        cram[:,i] = b[:]
        xs[i] = det(cram)/det(a)
    return xs

def newt2print(a,xi):
    print('f(x) =',a[0],'+',a[1],'(x-',xi[0],')','+',a[2],'(x-',xi[0],')(x-',xi[1],')')
    return 

def coeffs(xi):
    cf0 = xi[1]-xi[0]
    cf1 = xi[2]-xi[0]
    cf2 = cf1*(xi[2]-xi[1])
    c00 = c10 = c20 = 1.0
    c01 = c02 = 0.0
    c11 = cf0
    c12 = 0.0
    c21 = cf1
    c22 = cf2
    ci = array([[c00, c01, c02],[c10, c11, c12],[c20,c21,c22]])
    return ci

def newt2poly(xt,fxt):
    k = 0
    for i in range(n):
        xi = xt[k:k+3]
        fx = fxt[k:k+3]
        k = i + 2
        ci = coeffs(xi)
        a = cramer(ci,fx)
        newt2print(a,xi)

#dataset
xt = array([1.0, 3.0, 4.0, 6.0, 9.0])
fxt = array([4.0, 3.5, 2.9, 2.5, 2.75])
n = int((len(xt)-1)/2)
 
newt2poly(xt,fxt)
