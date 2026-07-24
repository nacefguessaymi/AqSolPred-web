"""Single-molecule Mordred descriptor computation."""

from __future__ import annotations
import mordred
import numpy as np
from rdkit.Chem.rdchem import Mol

from aqsolpred_web.compute.descriptor_groups import GROUPS_BY_DESC_TYPE


def predefined_mordred(
    mol: Mol, desc_type: str = "best", desc_names: bool = False
) -> list[str] | np.NDArray:
    """Compute (or list) Mordred descriptors for a molecule.

    Args:
        mol: RDKit molecule to compute descriptors for.
        desc_type: Which descriptor group to compute. One of "best", "all",
            "atom", "bond", "topological", "index", "ring", or "estate".
            Unrecognized values register no descriptors.
        desc_names: If True, return only the list of descriptor names
            instead of computing values (`mol` is still required but its
            value is unused in this mode).

    Returns:
        If `desc_names` is True, a list of descriptor name strings.
        Otherwise, the computed descriptor values for `mol`.
    """
    calc1 = mordred.Calculator()

    for register in GROUPS_BY_DESC_TYPE.get(desc_type, []):
        register(calc1)

    if desc_names:
        return [str(desc) for desc in calc1.descriptors]

    results = calc1(mol)
    return results._values
