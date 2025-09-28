import pandas as pd

df = pd.read_csv(r'\PortalKidsOperaciones\students\Jalarconm\data\bronze\orders.csv', sep = ',')

print(df)
print("shape",df.shape)
print(df.head())
print(df.dtypes)
print(df.columns.tolist())
print(len(df))
