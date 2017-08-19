from numpy import linspace, zeros,cos

x = linspace(0,2,10) 
n = len(x)
y = zeros(n) 

for i in range(n):
    y[i] = cos(x[i])
    print('%8.4f ' % y[i])
