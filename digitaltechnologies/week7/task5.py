# 20x + 10y = 350
# 17x + 22y = 500
import numpy as np

A = np.array([[1, 7], [2, 1]])
B = np.array([9, 18])
X = np.linalg.solve(A, B)

print(X)