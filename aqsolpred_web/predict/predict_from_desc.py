import pickle
from collections.abc import Sequence
from pathlib import Path

import pandas as pd
from rdkit.Chem.rdchem import Mol

from aqsolpred_web.compute import compute_descriptors
from aqsolpred_web.core import (
    DEFAULT_MODELS_DIR,
    MLP_MODEL_FILENAME,
    XGB_MODEL_FILENAME,
)


def predict_logs_from_descriptors(
    descriptors: pd.DataFrame, models_dir: Path = DEFAULT_MODELS_DIR
) -> list[float]:
    """Predict LogS from a precomputed descriptor matrix.

    Args:
        descriptors: Descriptor matrix as produced by
            `compute.compute_descriptors`.
        models_dir: Directory containing the pickled model files named by
            `core.constants.MLP_MODEL_FILENAME` and
            `core.constants.XGB_MODEL_FILENAME`.

    Returns:
        Predicted LogS values, one per row of `descriptors`.
    """
    mlp_model_import = pickle.load(open(models_dir / MLP_MODEL_FILENAME, "rb"))
    xgboost_model_import = pickle.load(open(models_dir / XGB_MODEL_FILENAME, "rb"))

    pred_mlp = mlp_model_import.predict(descriptors)
    pred_xgb = xgboost_model_import.predict(descriptors)
    pred_consensus = (pred_mlp + pred_xgb) / 2

    return list(pred_consensus)
