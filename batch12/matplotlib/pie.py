import matplotlib.pyplot as plt
import numpy as np
mylables=["Apple","banana","mango","orange"]
y = np.array([35, 25, 25, 15])

plt.pie(y,labels=mylables)
plt.legend()
plt.show() 