import numpy as np
import matplotlib.pyplot as plt

X_data = np.random.random(50) * 100
y_data = np.random.random(50) * 100

#print(X_data, y_data)

plt.scatter(X_data, y_data)
plt.show()
