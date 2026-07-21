"""Predict LogS for a DataFrame containing a SMILES column."""

from pathlib import Path

from rdkit import Chem
import pandas as pd

from aqsolpred_web.core import DEFAULT_MODELS_DIR
from aqsolpred_web.predict.predict_from_mol import calculate_logs
