import numpy as np
import matplotlib.pyplot as plt


def codingstair_sin(x):
    return np.sin(x)

def codingstair_cos(x):
    return np.cos(x)

x = np.linspace(-np.pi, np.pi)  #-pi부터 pi까지
y_sin = codingstair_sin(x)
y_cos = codingstair_cos(x)

plt.plot(x, y_sin, label="sin")
plt.plot(x, y_cos, label="cos")
plt.legend()
plt.xlabel("X", size=14)
plt.ylabel("Y", size=14)
plt.grid

plt.show()