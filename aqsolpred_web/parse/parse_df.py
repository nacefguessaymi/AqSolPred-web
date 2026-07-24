"""Parser functions for reading data from a DataFrame built
from a csv."""

from __future__ import annotations

import pandas as pd


def find_smiles(df: pd.DataFrame) -> str:
    """Find the SMILES column in a DataFrame, matching any column whose
    name contains "smile" (case-insensitive) - e.g. "SMILES",
    "canonical_smiles", "isosmiles".

    Args:
        df: DataFrame to search.

    Returns:
        The actual column name (original case preserved) that matched.

    Raises:
        ValueError: If no column matches, or more than one does.
    """
    matches: list[str] = df.columns[
        df.columns.str.contains("smile", case=False)
    ].tolist()

    if not matches:
        raise ValueError(
            f"No SMILES-like column found. Available columns: {list(df.columns)}"
        )
    if len(matches) > 1:
        raise ValueError(f"Multiple SMILES-like columns found: {matches}")
    return matches[0]
