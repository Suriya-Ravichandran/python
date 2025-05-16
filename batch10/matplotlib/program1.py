import matplotlib.pyplot as plt
import numpy as np


y=np.array([6,10,8,7,9])


mylabel=["Car","bike","Van","bus","turck"]

plt.pie(y,labels=mylabel)
plt.legend()
plt.show()