import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-1000,1000,1000000)
y=x**2
plt.plot(y,x)
plt.show()