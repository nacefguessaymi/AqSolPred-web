"""Predict LogS for a DataFrame containing a SMILES column."""

from pathlib import Path

import pandas as pd
from rdkit import Chem

from aqsolpred_web.core import DEFAULT_MODELS_DIR
from aqsolpred_web.parse import find_smiles
from aqsolpred_web.predict.predict_from_mol import calculate_logs


def predict_logs_from_df(
    df: pd.DataFrame, models_dir: Path = DEFAULT_MODELS_DIR
) -> pd.DataFrame:
    """Predict LogS for every row of a DataFrame that has a SMILES column.

    Args:
        df: DataFrame containing a column matching "smiles"
            (case-insensitive substring match; see `find_smiles`).
        models_dir: Directory containing the pickled model files.

    Returns:
        A copy of `df` with a new "LogS" column appended, in the same
        row order as the input.
    """
    smiles_col = find_smiles(df)
    molecules = [Chem.MolFromSmiles(smi) for smi in df[smiles_col]]
    logs = calculate_logs(molecules, models_dir)

    result = df.copy()
    result["LogS"] = logs
    return result
