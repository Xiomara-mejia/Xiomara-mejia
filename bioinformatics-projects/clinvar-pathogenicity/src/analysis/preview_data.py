import pandas as pd
from pathlib import Path

path = Path("data/raw/variant_summary.txt")

df = pd.read_csv(path, sep="\t", nrows=5, low_memory=False)

print("✅ Columns in this file:\n")
print(df.columns.tolist())

print("\n🧬 Preview of first 5 rows:\n")
print(df.head())

