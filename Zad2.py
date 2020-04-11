from matplotlib import pyplot as plt
import numpy as np

x, y = np.loadtxt('file.txt', delimiter=',', unpack=True)


plt.plot(x, y, color='b', linestyle='', marker='.')

plt.show()