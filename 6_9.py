from numpy import array,dot
A = array([[1,2,3],[4,5,6],[7,8,9]])
B = array([[-1,1,2],[5,4,2],[3,1,-2]])
mmt = A * B
dotp = A.dot(B)
print('matrix multiplication = ',mmt)
print('dot product = ',dotp)
