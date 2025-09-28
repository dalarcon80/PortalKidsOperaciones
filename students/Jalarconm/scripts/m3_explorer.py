import pandas as pd

df = pd.read_csv('dalarcon80/PortalKidsOperaciones/students/Jalarconm/data/bronze/customers.csv', sep = ',')

print(df)
print("Shape:",df.shape)
print("Head: "df.head())
print("Dtypes: "df.dtypes)
print("Columns: "df.columns.tolist())
print("Len: ", len(df))
