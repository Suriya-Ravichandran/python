import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("data.csv")
df.plot()
plt.show()
print(df.head(30))
finaldata=df.to_json()
f=open("data.json","w")
f.write(finaldata)