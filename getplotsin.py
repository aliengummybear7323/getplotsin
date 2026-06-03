# Finds the sin of some numbers and plots them with matplotlib
import numpy as np
import sys
import matplotlib.pyplot as plt

try:
    int1 = float(input("Enter a number: "))
    int2 = float(input("Enter another number: "))
    stepsize = float(input("Enter the step size: "))
    print(f"Drawing the sinewave of all numbers between {int1} and {int2}")
    plt.style.use("ggplot")

    if int1 < int2:
        x = np.arange(int1, int2, stepsize)
    elif int1 > int2:
        x = np.arange(int2, int1, stepsize)
    else:
        print("Sorry, those 2 numbers cannot be the same. Try again")
        sys.exit(0)

    y = np.sin(x)

except KeyboardInterrupt:
    print("\nGoodbye...")
    sys.exit(0)
except ValueError:
    print("Sorry, that is invalid!")
    sys.exit(0)

plt.plot(x, y)
plt.show()

