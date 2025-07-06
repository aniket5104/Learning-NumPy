import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

np.stack((a, b))       
# Output: 
# [[1 2 3]
#  [4 5 6]]  → shape (2, 3)

np.stack((a, b), axis=1) 
# Output:
# [[1 4]
#  [2 5]
#  [3 6]]  → shape (3, 2)
