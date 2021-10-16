import numpy as np

def first_func(x):   #first_func라는 이름의 Python 함수로 표현
    return 2*x+1   #2x+1

x = 1   #글로벌 변수라서 위의 x와 다름
y = first_func(x)
print(y)