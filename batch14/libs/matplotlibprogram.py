import matplotlib.pyplot as plt
import numpy as np

x=[10,20,30,40,50]
y=[18,10,29,30,40]
mylabes=["apple","graphs","orange","banana","pineapple"]
plt.pie(np.array(y),labels=mylabes)
plt.legend()
plt.show()

