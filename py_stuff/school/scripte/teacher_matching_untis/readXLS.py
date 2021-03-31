from collections import defaultdict
from read_html import all_untis_teachers as a_u_t
import pandas as pd

DATA_FILE = "Lehrerliste-5er-25.03.2021.xlsx"
dd =defaultdict(list)

df = pd.read_excel(DATA_FILE, usecols=["Lehrer"])
#print(type(df))

temp = df.to_dict()
dict =temp.get('Lehrer')
#print(dict[0])

lehrer_jgst5 = {}

for key,value in dict.items():
    if value not in lehrer_jgst5.values() and pd.isna(value) == False and len(value) == 3:
        lehrer_jgst5[key] = value
temp = {}
for key,value in lehrer_jgst5.items():
        #print(value)
        print(a_u_t[value])
        temp[value] = a_u_t[value]

#print(lehrer_jgst5)
#print(len(lehrer_jgst5))
lehrer_jgst5.clear()
lehrer_jgst5 = temp
print(lehrer_jgst5)
#print(len(lehrer_jgst5))

#print(a_u_t)
print(len(dict))
#print(len(result))

