import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2])
pielabels=["apple","mango","banana","orange","graphs"]

plt.pie(x,labels=pielabels)
plt.legend()
plt.show()