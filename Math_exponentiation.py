import numpy as np
import matplotlib.pyplot as plt

def expo_func(x):
    a = 4
    return x**a

x = np.linspace(0,2)
y = expo_func(x)

plt.plot(x,y)
plt.xlabel("X", size=15)
plt.ylabel("Y", size=15)
plt.grid
plt.show()