import numpy as np
import matplotlib.pyplot as plt

def codigstair1(x):
    return 2*x

def codingstair2(x):
    return 3*x

x=np.linspace(-5, 5)
y_1 = codigstair1(x)
y_2 = codingstair2(x)

plt.plot(x, y_1, label="1")
plt.plot(x, y_2, label="2")
plt.legend()
plt.xlabel("X", size=14)
plt.ylabel("Y", size=14)
plt.grid

plt.show()