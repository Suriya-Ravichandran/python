import pandas as pd

# Read the CSV file
data = pd.read_csv("data.csv")

# Get the first 10 rows
result1 = data.head(10)

# Get rows from index 10 to 19 (11th to 20th row)
result2 = data.iloc[10:20]

# Print the first result
print(result1)

# Optionally, print the second result
print(result2)
