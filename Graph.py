import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.xlabel('Time')
plt.ylabel('Some function of time')
plt.title('My cool chart')
plt.show()
