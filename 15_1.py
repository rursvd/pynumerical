from numpy import array
from numpy.linalg import det

a = array([[4,1,-1],[3,-1,2],[-1,2,3]])
b = array([-2,1,1])
a1 = array([[-2,1,-1],[1,-1,2],[1,2,3]])
a2 = array([[4,-2,-1],[3,1,2],[-1,1,3]])
a3 = array([[4,1,-2],[3,-1,1],[-1,2,1]])
detA = det(a)
detA1 = det(a1)
detA2 = det(a2)
detA3 = det(a3)
print('|A| = ',detA, '|A1| = ',detA1,'|A2| = ',detA2,'|A3| = ',detA3)
x1 = detA1/detA
x2 = detA2/detA
x3 = detA3/detA
print('x1 = ',x1,'x2 = ',x2,'x3 =',x3)

