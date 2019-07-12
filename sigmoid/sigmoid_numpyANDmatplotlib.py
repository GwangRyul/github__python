import numpy as np
import matplotlib.pylab as plt

def sigmoid(x):
    return (1 / (1 + np.exp(-x)))

# numpy를 이용하여 sigmoid함수 출력
#x = np.array([-1., 1., 2.])
#print(sigmoid(x))

# matplotlib를 이용한 sigmoid함수 그래프 출력
x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()
