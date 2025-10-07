from __future__ import annotations
import argparse
from pathlib import Path
from src.analysis.pathogenicity_analysis import load_data, summarize, count_by_label


def main():
    parser = argparse.ArgumentParser(description="ClinVar Pathogenicity CLI")
    parser.add_argument("--csv", required=True, help="Path to ClinVar CSV (in data/raw/)")
    parser.add_argument("--label-col", default="ClinicalSignificance", help="Label column name")
    parser.add_argument("--summary", action="store_true", help="Print dataframe summary")
    parser.add_argument("--counts", action="store_true", help="Print label counts")
    args = parser.parse_args()

    df = load_data(Path(args.csv))
    if args.summary:
        print(summarize(df))
    if args.counts:
        print(count_by_label(df, args.label_col))


if __name__ == "__main__":
    main()
