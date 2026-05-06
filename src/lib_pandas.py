import pandas as pd


# series = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])

# print(series)

# data = {
#     "nombre": ["Deivis", "Samuel", "Cedeño"],
#     "edad": [15, 18, 16],
# }

# df = pd.DataFrame(data)

# print(df.loc[[0,2]])


df = pd.read_csv("src/data.csv")

print(df.to_string())