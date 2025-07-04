import numpy as np
#From Python list or tuples
arr1= np.array([1,3,5,7]) #1d array
arr2= np.array([[1,2],[3,4]])#2d array
# print(type(arr1))   #<class 'numpy.ndarray'>
# print(type(arr2))   #<class 'numpy.ndarray'>


#Predefined arrays
arr3=np.zeros((2,3)) #an array of order 2*3, all elements =0
arr4=np.ones((3,3)) #an array of order 3*3, all elements =1
arr5=np.full((2,3),7) #an array of order 2*3, all elements= 7
iden_matrix=np.eye(3) #an identity matrix of order 3*3
print(arr3," \n\n",arr4,"\n\n",arr5,"\n\n",iden_matrix)

#Uninitialised array:
empty_arr=np.empty((2,2))
print(empty_arr)

# float_arr=np.array([1,2,3],dtype=float) #all elements are of float datatype
# print(float_arr,"\n")

