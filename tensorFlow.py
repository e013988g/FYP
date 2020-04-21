import numpy as np
%matplotlib inline import matplotlib.pyplot as plt

x = np.arange(0, 5, 0.1);
y = np.sin(x)

plt.plot(x, y)