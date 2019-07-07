import numpy as np
radix = 2

dataWidth = 8
dataDepth = 256

f=open('RAM_data.coe', 'w')
f.write('memory_initialization_radix=')
f.write(str(radix))
f.write(';\n')
f.write('memory_initialization_vector=\n')
ramData = np.random.randint(2, size=(dataDepth, dataWidth))
np.savetxt(f,ramData, fmt="%1d", delimiter="")
f.close()