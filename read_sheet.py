import json
import pandas as pd

data = pd.read_excel (r"chamados_cmpc.xlsx")
#print(data)
df = pd.DataFrame(data, columns=['Analista','CMPC'])
#result = df.to_json()
print(df)