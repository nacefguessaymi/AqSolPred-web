"""CSV reading for report DataFrames."""

from pathlib import Path

import pandas as pd


def read_csv(csv_file: Path) -> pd.DataFrame:
    """Read a csv file and create a DataFrame from
    it. Needed for processing SMILES from a csv if
    calculating LogS from a csv.
    Args:
        csv_file: Path to the csv to get LogS from. Needs
                  a 'smiles' column.
    """
    if csv_file.exists():
        df = pd.read_csv(csv_file)
    else:
        raise FileNotFoundError(
            f"Could not find file {csv_file}. Make sure the path exists."
        )
    return df
