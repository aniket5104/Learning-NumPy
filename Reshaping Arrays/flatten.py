import numpy as np

arr= np.arange(1,13).reshape(3,4)
flat_copy=arr.flatten()
print("Original array: \n",arr)
print("Flattened array: \n",flat_copy)
flat_copy[0]=100
print("Original Array: /n",arr) #flatten makes a new copy of array due to which change in flattened array doesnot reflect in original array