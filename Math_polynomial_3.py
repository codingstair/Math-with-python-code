import numpy as np
import matplotlib.pyplot as plt


def polynomial_func(x):
    return 3*x**3 + 2*x**2 + 1

x = np.linspace(-3, 3)
y = polynomial_func(x)

plt.plot(x,y)
plt.xlabel("X", size=14)
plt.ylabel("Y", size=14)
plt.grid
plt.show()