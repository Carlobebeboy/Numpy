import numpy as np

B = np.arange(1,101,1)

A = np.reshape(B,(10,10))

square = np.square(A) 

C = square[square % 3 == 0]

print(C)