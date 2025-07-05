import pandas as pd
from matplotlib import pyplot

data="data.csv"

df=pd.read_csv(data)

df.plot()
pyplot.show()