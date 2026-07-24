"""Model-ready descriptor matrix computation for sets of RDKit molecules."""

from __future__ import annotations
from collections.abc import Sequence
from typing import cast

import pandas as pd
from loguru import logger
from rdkit import Chem
from rdkit.Chem import rdMolDescriptors
from rdkit.Chem.rdchem import Mol

from aqsolpred_web.compute.constants import SELECTED_COLUMNS
from aqsolpred_web.compute.mordred_descriptors import predefined_mordred


def compute_descriptors(molecules: Sequence[Mol]) -> pd.DataFrame:
    """Compute the Mordred descriptors used by the AqSolPred models for a
    sequence of RDKit molecules.

    This is the shared implementation used by both `web.app` (SMILES
    input) and `cli.report` (SDF input, via `main.calculate_logS`).

    Args:
        molecules: RDKit `Mol` objects to compute descriptors for.

    Returns:
        A DataFrame indexed by molecular formula, with one column per
        descriptor in `SELECTED_COLUMNS`, coerced to numeric (NaN -> 0).
    """
    formulas: list[str] = []
    all_descriptors: list = []

    for mol in molecules:
        mol_with_hs = Chem.AddHs(mol)
        formula = rdMolDescriptors.CalcMolFormula(mol_with_hs)
        formula = formula.replace("+", "").replace("-", "")

        formulas.append(formula)
        all_descriptors.append(predefined_mordred(mol_with_hs, "all"))

    column_names = predefined_mordred(Chem.MolFromSmiles("CC"), "all", True)

    descriptors_df = pd.DataFrame(
        index=formulas, data=all_descriptors, columns=column_names
    )
    selected = descriptors_df[SELECTED_COLUMNS]
    selected = selected.apply(pd.to_numeric, errors="coerce")
    selected = selected.fillna(0)

    nan_cols = selected.columns[selected.isna().any()].to_list()
    if nan_cols:
        logger.warning(f"{len(nan_cols)} descriptors failed: {nan_cols[:5]}....")

    return cast(pd.DataFrame, selected)
