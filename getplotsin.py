# Finds the sin of some numbers and plots them with matplotlib
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 20, 0.1)
y = np.sin(x)
plt.plot(x, y)