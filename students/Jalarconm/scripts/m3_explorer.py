import pandas as pd

df = pd.read_csv('dalarcon80/PortalKidsOperaciones/students/Jalarconm/data/bronze/customers.csv', sep = ',')

print(df)
print("Shape:",df.shape)
print("Head: "df.head())
print(df.dtypes)
print(df.columns.tolist())
print(len(df))
