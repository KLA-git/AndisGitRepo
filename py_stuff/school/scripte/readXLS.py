from collections import defaultdict

import pandas as pd

DATA_FILE = "Lehrerliste-5er-25.03.2021.xlsx"
dd =defaultdict(list)

df = pd.read_excel(DATA_FILE, usecols=["Lehrer"])
print(type(df))

temp = df.to_dict()
dict =temp.get('Lehrer')
print(dict[0])

result = {}

for key,value in dict.items():
    if value not in result.values():
        result[key] = value

print(result)
print(len(dict))
print(len(result))

