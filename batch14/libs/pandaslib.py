import pandas as pd

data="data.csv"

df=pd.read_csv(data)
print(df.tail(10))