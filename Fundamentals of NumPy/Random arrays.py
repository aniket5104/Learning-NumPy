import numpy as np

random_array= np.random.random((3,4))# generates an array of order 3*4 with random elements
uniform_arr= np.random.rand(2,3) #uniform [0,1)
standard_arr= np.random.randn(3,3) #standard normal(centered around zero)
int_arr=np.random.randint(0,10,size= (2,3))
print(random_array,"\n\n",uniform_arr,"\n\n",standard_arr,"\n\n",int_arr)
