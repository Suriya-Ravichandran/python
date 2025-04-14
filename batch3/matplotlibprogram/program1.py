import matplotlib.pyplot as plt
import numpy as np

# x=np.array([1,2,3,4,5])
y=np.array([10,20,30,40,50])
mylabels = ["Apples", "Bananas", "Cherries", "Dates","orange"]

plt.pie(y,labels=mylabels)
plt.show()