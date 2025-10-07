from __future__ import annotations
import pandas as pd
from pathlib import Path


def load_data(path: str | Path) -> pd.DataFrame:
    """
    Load a large ClinVar dataset in chunks to avoid memory issues.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Data not found: {path}")

    chunks = []
    for chunk in pd.read_csv(path, sep="\t", chunksize=100000, low_memory=False):
        chunks.append(chunk)
    df = pd.concat(chunks, ignore_index=True)
    return df


def summarize(df: pd.DataFrame) -> pd.DataFrame:
    """
    Return a basic summary of the dataset.
    """
    return df.describe(include="all")


def count_by_label(df: pd.DataFrame, label_col: str = "ClinicalSignificance") -> pd.Series:
    """
    Count how many of each label type exist (e.g., Pathogenic vs. Benign)
    and save the results to a CSV file.
    """
    if label_col not in df.columns:
        raise KeyError(f"Column '{label_col}' not in dataframe")

    counts = df[label_col].value_counts(dropna=False)

    # 💾 Save counts to CSV
    output_path = Path("reports/pathogenicity_counts.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    counts.to_csv(output_path)
    print(f"✅ Counts saved to {output_path}")

    return counts


