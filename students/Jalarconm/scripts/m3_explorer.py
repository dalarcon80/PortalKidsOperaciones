import pandas as pd

df = pd.read_csv(r'C:\Users\sarac\Portalkids\PortalKidsOperaciones\students\Jalarconm\data\bronze\products.csv', sep = ',')

print(df)
df.shape
print("shape",df.shape)