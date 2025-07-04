import numpy as np
arr= np.array([1,2,3,4,5])
shallow_copy=arr.view()
deep_copy= arr.copy()
deep_copy[0]=100
print("Array after deep copy: \n",arr)
shallow_copy[0]=100
print("Array after shallow copy: \n",arr) #in shallow copying the 