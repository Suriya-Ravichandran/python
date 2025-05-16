import matplotlib.pyplot as pt
import numpy as np



y=np.array([6,8,10,7,9])

mylabel=["Apple","Graph","orange","mango","pineapple"]


pt.pie(y,labels=mylabel)
pt.legend()
pt.show()

