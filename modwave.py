import numpy as np
import matplotlib.pyplot as plt

xlim = 10e-2

x = np.arange(0, xlim, 10e-9)
y = 2000*np.sin(10e9*x)*np.sin(10e3*x)

np.savetxt("mod_data.txt", y, fmt="%d", delimiter = "")
# plt.plot(x,y)
# plt.show()