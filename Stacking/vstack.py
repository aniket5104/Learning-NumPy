import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.vstack((a, b))
print(result)
# Output:
# [[1 2 3]
#  [4 5 6]]
