import numpy as np
import matplotlib.pyplot as plt

x = []
y = []
total = 0  # 모든 경우의 수
num = 0  # 1/10이 나오는 경우의 수
n = 1000  # 시행 수

for i in range(n):

    if np.random.randint(10) == 1:
        num += 1

    total += 1
    x.append(i)
    y.append(num/total)

plt.plot(x,y)
plt.plot(x, [1/10]*n)  # 기준선

plt.xlabel("X")
plt.ylabel("Y")
plt.grid
plt.show()