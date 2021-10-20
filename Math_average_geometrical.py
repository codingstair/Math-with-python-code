import numpy as np

x = np.array([10,20,25,30,50])

base = 1
for xn in x:
    base *= xn
geometric_mean = base ** (1/len(x))

print(geometric_mean)