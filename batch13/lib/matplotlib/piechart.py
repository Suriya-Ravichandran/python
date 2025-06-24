import numpy as np
from matplotlib import pyplot as plt

x=np.array([10,50,30,40])
mylables=["apple","mango","orange","graphs"]
mycolor=["red","green","blue","black"]
plt.pie(x ,labels=mylables,colors=mycolor)
plt.legend()
plt.show()