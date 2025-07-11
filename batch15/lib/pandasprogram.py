import pandas as pd

# data={
#     "time":[20,30,50,60],
#     "km":[3,5,6,7]
# }

# dataframe=pd.DataFrame(data)
# print(dataframe)

data="data.csv"

df=pd.read_csv(data)
print(df.tail(10)) 