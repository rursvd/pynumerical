from numpy import array

x = array([1,2,3,4,5])
fx = array([1,4,9,16,25])

n = len(x) -1 
h = (x[n] - x[0])/n
simp = 0.0
print(h)

for i in range(1,n):
    if (i % 2) == 1:
        simp = simp + 4.0 * fx[i]
    else:
        simp = simp + 2.0 * fx[i]
simp = h*(fx[0] + simp + fx[n])/3.0 

print('T = %8.4f' % simp)
