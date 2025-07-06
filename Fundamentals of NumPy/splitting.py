import numpy as np

#hsplit 
a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8]])

result = np.hsplit(a, 2)

#vsplit
a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8]])

result = np.vsplit(a, 2)
