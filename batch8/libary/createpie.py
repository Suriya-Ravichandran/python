import matplotlib.pyplot as mp
import numpy as np

data=np.array([30,40,20,10])
datalabels=["Apple","Graph","Orange","Pine apple"]
# myexplode = [0.2, 0, 0.2, 0]
mp.pie(data,labels=datalabels)
mp.legend(title="Fruits List")
mp.show()
