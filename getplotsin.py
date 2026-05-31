# Finds the sin of some numbers and plots them with matplotlib
import numpy as np
import sys
import matplotlib.pyplot as plt
try:
	int1 = int(input("Enter a number: "))
	int2 = int(input("Enter another number: "))
	print(f"Drawing the sinewave of all numbers between {int1} and {int2}")
	plt.style.use("ggplot")
	x = np.arange(int1, int2, 0.1)
	y = np.sin(x)
	plt.plot(x, y)
	plt.show()
except KeyboardInterrupt:
	sys.exit(0)
