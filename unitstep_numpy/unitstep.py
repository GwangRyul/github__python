import numpy as np
import matplotlib.pylab as plt

def step_function(x): #x는 numpy로 이루어진 배열이여만 한다.
    y = x > 0
    return y.astype(np.int)

def step_function_matplotlib(x):
    return np.array(x > 0, dtype = np.int)

#numpy를 이용한 계단함수 출력
x = np.array([-1. ,1. , 2.])
print(step_function(x))

#matplotlib를 이용하여 계단함수 그래프 출력
x = np.arange(-5., 5., 0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()
