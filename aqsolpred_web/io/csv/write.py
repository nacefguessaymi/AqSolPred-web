"""CSV writing for report DataFrames."""

from pathlib import Path

import pandas as pd


def write_csv(df: pd.DataFrame, csv_file: Path) -> None:
    """Write a DataFrame to a CSV file, creating parent directories if needed.

    Args:
        df: DataFrame to write.
        csv_file: Path to write the CSV file to.
    """
    if not csv_file.parent.exists():
        csv_file.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(csv_file, index=False)
