import numpy as np

#round --->  rounds to nearest int
a=np.random.random((3,4))*100
print(a)
# print(np.round(a))

#floor ---> rounds to nearest lower int
# print(np.floor(a))

#ceil ---> rounds to nearest upper int
print(np.ceil(a))