import numpy as np

x = np.array([10,20,25,30,50])

avr_x = len(x)/(np.sum(1/x))  # 표본 개수 / (1/x의 합계)

print(np.sum(1/x))  # 1/x의 합계
print(avr_x)  # 조화평균