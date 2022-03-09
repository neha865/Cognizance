import numpy as np
a = np.array([10,11,12,13,14])
nz = 5
Z0 = np.zeros(len(a) + (len(a)-1)*(nz))
Z0[::nz+1] = a
print(np.floor(Z0))
