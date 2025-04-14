import pandas as pn

import matplotlib.pyplot as plt

data=pn.read_csv("data.csv")
data.plot()
plt.show()
# print(data.to_string())