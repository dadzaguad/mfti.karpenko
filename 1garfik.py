import numpy as np

x = np.array([1, 10, 1000])
print((np.log((1 / np.e ** (np.sin(x) + 1)) / ((5 / 4) + 1 / x ** 15))) / np.log(1 + x ** 2))
