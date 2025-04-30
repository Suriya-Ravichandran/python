import matplotlib.pyplot as plot

import numpy as np

x=np.array([10,20,30,90])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plot.pie(x,labels=mylabels)
plot.show()