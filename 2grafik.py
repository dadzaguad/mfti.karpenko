import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-20, 20, 100)
plt.title('y(x) = x*x - x - 6')
plt.plot(x, x * x - x - 6)
plt.show()
