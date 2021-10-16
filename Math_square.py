import numpy as np
import matplotlib.pyplot as plt

def squ_fucn(x):
    return np.sqrt(x)

x = np.linspace(0, 5)
y = squ_fucn(x)

plt.plot(x,y)
plt.xlabel("X", size=15)
plt.ylabel("Y", size=15)
plt.grid
plt.show()