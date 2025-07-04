import numpy as np

#1d array
arr=np.array([10,20,30,40,50])
print(arr[[1,3,4]])

#2d array
mat= np.array([[10,20,30],
               [40,50,60],
               [80,90,40]])
xcoor=[0,1,2]
ycoor=[1,2,0]
print(mat[xcoor,ycoor])
