from collections.abc import Sequence
from pathlib import Path

from rdkit import Chem
from rdkit.Chem.rdchem import Mol

from aqsolpred_web.core import DEFAULT_MODELS_DIR
from aqsolpred_web.compute import compute_descriptors
from aqsolpred_web.predict.predict_from_desc import predict_logs_from_descriptors


def calculate_logs(
    molecules: Sequence[Mol], models_dir: Path = DEFAULT_MODELS_DIR
) -> list[float]:
    """Predict LogS for a list of molecules, end to end.

    Computes descriptors for `molecules` and predicts LogS from them in
    one step. If you already have a descriptor matrix (e.g. because you
    also need it for display, as `web/app.py` does), call
    `predict_logS_from_descriptors` directly instead to avoid computing
    descriptors twice.

    Args:
        molecules: RDKit molecules to compute LogS for.
        models_dir: Directory containing the pickled model files (see
            `predict_logS_from_descriptors`).

    Returns:
        Predicted LogS values, one per molecule. Index `i` corresponds to
        `molecules[i]`.
    """
    descriptors = compute_descriptors(molecules)
    return predict_logs_from_descriptors(descriptors, models_dir)


def predict_logs_single(smiles: str, models_dir: Path = DEFAULT_MODELS_DIR) -> float:
    """Predict LogS for a single SMILES string.

    Args:
        smiles: The smiles string of the molecule being
        predicted
        models_dir: Path to the directory containing the
        pickled model files
    """
    mol = Chem.MolFromSmiles(smiles)
    return calculate_logs([mol], models_dir)[0]
