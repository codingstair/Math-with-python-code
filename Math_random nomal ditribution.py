import matplotlib.pyplot as plt
import numpy as np

n =2000
x = np.random.randn(n)   #randn : 정규분포
y = np.random.randn(n)

plt.scatter(x,y)
plt.show()