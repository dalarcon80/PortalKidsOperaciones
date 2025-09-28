from pathlib import Path
import pandas as pd

df = pd.read_csv(Path("sources/orders_seed.csv"))
print("df.shape =", df.shape) 
print("df.columns =", df.columns.tolist())
print("Head:")
print(df.head().to_string())
print("Dtypes:")
print(df.dtypes)
