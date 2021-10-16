import matplotlib.pyplot as plt
import numpy as np

n =2000
x = np.random.rand(n)
y = np.random.rand(n)

plt.scatter(x,y)   # 산포도
plt.show()