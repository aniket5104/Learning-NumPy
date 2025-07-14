import numpy as np

arr=np.arange(1,11).reshape(2,5)
print("Original Array:\n",arr)
flat=arr.ravel()
print("flattened array: \n",flat)
flat[0]=100
print("Original array: \n",arr) #flattened array and original array share same memory location