import numpy as np
import matplotlib.pyplot as plt

def codingstair(x):
    return  3*x**2 + 2*x - 9

x = np.linspace(-np.pi, np.pi)
y_x = np.abs(codingstair(x))

plt.plot(x, y_x, label='abs')
plt.legend
plt.xlabel("x", size=14)
plt.ylabel("y", size=14)
plt.show()