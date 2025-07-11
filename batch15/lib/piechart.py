import numpy as np
from matplotlib import pyplot

x=np.array([10,20,30,40,50])
mylabel=["apple","mango","banana","graphs","pine apple"]
pyplot.pie(x,labels=mylabel)
pyplot.legend(title="fruits")

pyplot.show()
