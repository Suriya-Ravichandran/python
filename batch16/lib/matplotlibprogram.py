from matplotlib import pyplot
import numpy as np

ydata=np.array([10,20,30,10,50])
mylabel=["apple","mango","graphs","orange","pine apple"]
myexplode=[0.2,0,0,0,0]
pyplot.pie(ydata,labels=mylabel,explode=myexplode)
pyplot.legend(title="Fruits")

pyplot.show()
