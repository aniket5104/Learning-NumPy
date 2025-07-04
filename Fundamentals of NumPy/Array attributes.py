import numpy as np

arr=np.random.random((2,3,4)) #only for 1d array

print(arr.ndim) #returns dimension of array
print(arr.size) #returns total no. of elements in array
print(arr.shape) #tuple showing dimension of array
print(arr.dtype) #data type of all elements
print(arr.itemsize) #byte size of one array element
print(arr.nbytes) #total memory used
print(arr.T) #transpose of matrix(2d or more)