import numpy as np
a = input("enter the matrix with ; after each row : ")
m =np.matrix(a)
b = input("enter the matrix 2 with row matching with matrix 1 : ")
n =np.matrix(b)
print(m)
print(n)
m3 = np.dot(m,n) 
print(m3)