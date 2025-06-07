from tabulate import tabulate

data = [
    ["Tamil", 49],
    ["English", 49],
    ["Maths", 49]
]

headers = ["Subject","Marks"]

print(tabulate(data, headers=headers, tablefmt="grid"))