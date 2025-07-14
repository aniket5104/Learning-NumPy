import numpy as np

a=np.random.randint(0,13,size=(3,4))
print("Org Array\n",a)
sorted_array=np.sort(a,axis=None)
print("Flattened Sorted Array\n",sorted_array)

sorted_array=np.sort(a,axis=0)
print("Column wise Sorted Array\n",sorted_array)

sorted_array=np.sort(a,axis=1)
print("Row wise Sorted Array\n",sorted_array)

sorted_array=np.sort(a,axis=-1)
print("Array sorted across last axis\n",sorted_array)

sorted_array=np.sort(a,axis=None)[::-1]
print("Sorted Array in descending order\n",sorted_array)