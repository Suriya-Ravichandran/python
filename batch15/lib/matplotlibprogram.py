import numpy as np
from matplotlib import pyplot

x=np.array([10,20,30,40,50])
y=np.array([1,2,5,2,7])

pyplot.plot(x,y,marker="*",linestyle="dashed")

pyplot.xlabel("Average Pulse")
pyplot.ylabel("Calorie Burnage")
pyplot.show()