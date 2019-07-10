import numpy as np
radix = 2

dataWidth = 8
dataDepth = 256

ramData = np.random.randint(2, size=(dataDepth, dataWidth))
np.savetxt("tb_data.txt",ramData, fmt="%1d", delimiter="")