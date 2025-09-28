from pathlib import Path
import pandas as pd

df = pd.read_csv(Path("sources/orders_seed.csv"))
print("df.shape =", df.shape) 
print("df.columns =", df.columns.tolist())
print("Head:\n", df.head().to_string())
print("Dtypes:\n", df.dtypes)

