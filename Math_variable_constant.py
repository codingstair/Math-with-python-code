import numpy as np
import matplotlib.pyplot as plt

a=1
x=np.linspace(-5,5)
y=a*x

plt.plot(x,y)
plt.xlabel("X", size=15)
plt.ylabel("Y", size=15)
plt.grid
plt.show()