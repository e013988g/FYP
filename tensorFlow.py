import numpy as np
import matplotlib.pyplot as plt
print(matplotlib.get_backend())
x = np.arange(0, 5, 0.1);
y = np.sin(x)
plt.plot(x, y)