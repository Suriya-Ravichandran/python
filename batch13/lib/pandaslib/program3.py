import pandas as pd
from matplotlib import pyplot as plt

df=pd.read_csv("data.csv")

df.plot()
plt.show()

