# Finds the sin of some numbers and plots them with matplotlib

import math
import numpy as np
import sys
import matplotlib.pyplot as plt

try:
    int1 = float(input("Enter a number: "))
    int2 = float(input("Enter another number: "))
    freq_hz = float(input("Enter the mains input frequency in Hz: "))
    stepsize = float(input("Enter the step size: "))
    v_target = float(input("Enter the target voltage (V): "))
    cap_out = float(input("Enter the output capacitance (F): "))
    r_in = float(input("Enter the input (charging) resistance (ohms): "))
    r_out = float(input("Enter the output (load) resistance (ohms): "))

    plt.style.use("ggplot")
    if int1 < int2:
        x = np.arange(int1, int2, stepsize)
    elif int1 > int2:
        x = np.arange(int2, int1, stepsize)
    else:
        print("Sorry, those 2 numbers cannot be the same. Try again")
        sys.exit(0)

    v_in = np.sin(x * freq_hz * math.pi * 2)
    plt.plot(x, v_in)

    v_out = np.ndarray(x.shape)
    v_out[0] = 0

    for i in range(x.shape[0]):
        v_out[i] = v_out[i - 1] - 1 / (r_out * cap_out)
        if v_out[i] < v_target and v_in[i] > v_target:
            v_out[i] += (v_in[i] - v_out[1]) / (r_in * cap_out)
            v_out[i] = max(v_out[i], v_in[i])

    plt.plot(x, v_out)
    plt.show()
except KeyboardInterrupt:
    print("\nExiting...")
except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)
