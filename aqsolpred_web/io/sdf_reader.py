"""SDF file reading."""

from pathlib import Path

import pandas as pd
from rdkit import Chem


def read_sdf(sdf_file: Path) -> pd.DataFrame:
    """Read molecules from an SDF file into a DataFrame.

    Args:
        sdf_file: Path to the SDF file.

    Returns:
        A DataFrame with "Name" and "SMILES" columns, one row per molecule.
    """
    molecules = Chem.SDMolSupplier(
        str(sdf_file), sanitize=True, removeHs=False, strictParsing=True
    )
    records = [
        {"Name": mol.GetProp("_Name").strip(), "SMILES": Chem.MolToSmiles(mol)}
        for mol in molecules
    ]
    return pd.DataFrame(records, columns=[key for key in records])
