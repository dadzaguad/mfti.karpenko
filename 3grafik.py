import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-20, 20, 200)
plt.plot(x, np.log((x * x + 1) * np.exp(-abs(x) / 10)) / np.log(1 + np.tan(1 / (1 + np.sin(x) ** 2))))
plt.show()
