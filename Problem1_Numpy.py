import numpy as np

X = np.random.random((5,5))

A = np.mean(X)

B = np.std(X)

Z = (X - A)/B

print("Normalized: ", Z)