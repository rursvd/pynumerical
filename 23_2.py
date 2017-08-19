from numpy import array,mean,sum,linspace
from numpy.linalg import det

# dataset 
x = array([0, 1, 2, 4])  
y = array([2, 3, 9, 15])

n = len(x)
x1sm = sum(x)
y1sm = sum(y)
x2sm = sum(x**2)
x3sm = sum(x**3)
x4sm = sum(x**4)
xysm = sum(x*y)
x2ysm = sum((x**2)*y)

# Cramer's rule

eq = array([[x2sm,x3sm,x4sm],
             [x1sm,x2sm,x3sm],
             [n,x1sm,x2sm]])

rig = array([x2ysm, xysm, y1sm]) 

detabc = det(eq)

eqc = array([[x2ysm,x3sm,x4sm],
             [xysm,x2sm,x3sm],
             [y1sm,x1sm,x2sm]])
eqb = array([[x2sm,x2ysm,x4sm],
             [x1sm,xysm,x3sm],
             [n,y1sm,x2sm]])
eqa = array([[x2sm,x3sm,x2ysm],
             [x1sm,x2sm,xysm],
             [n,x1sm,y1sm]])

detc = det(eqc)
detb = det(eqb)
deta = det(eqa)
a = deta/detabc
b = detb/detabc
c = detc/detabc
print('a = ',a,'b = ',b,'c =',c)
