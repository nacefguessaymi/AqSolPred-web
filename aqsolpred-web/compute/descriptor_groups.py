"""Mordred descriptor-group registration.

Each `register_*` function adds the Mordred descriptors for one named
group onto an existing `mordred.Calculator`. The groupings mirror the
"best" / "atom" / "bond" / "topological" / "index" / "ring" / "estate"
categories used by the original AqSolPred model.

`GROUPS_BY_DESC_TYPE` maps a `desc_type` string (as accepted by
`predefined_mordred`) to the list of register functions that should run
for it. This preserves the original behavior exactly:
    - "best" registers only the "best" group.
    - "all" registers every group EXCEPT "best" (matching the original
      code, where the "best" block was gated on `desc_type == "best"`
      only, never on "all").
    - Any other recognized name (e.g. "ring") registers just that group.
"""

from collections.abc import Callable

import mordred
from mordred import (
    SLogP,
    Chi,
    ABCIndex,
    BondCount,
    Polarizability,
    RingCount,
    EState,
    RotatableBond,
    CarbonTypes,
    Aromatic,
    AtomCount,
    VdwVolumeABC,
    McGowanVolume,
    HydrogenBond,
)

RegisterFn = Callable[[mordred.Calculator], None]


def register_best(calc: mordred.Calculator) -> None:
    """Register the minimal "best" descriptor set onto `calc`."""
    calc.register(mordred.SLogP)
    calc.register(mordred.HydrogenBond.HBondAcceptor)
    calc.register(mordred.HydrogenBond.HBondDonor)
    calc.register(mordred.AtomCount.AtomCount("HeavyAtom"))
    calc.register(mordred.TopoPSA.TopoPSA(True))
    calc.register(mordred.RingCount.RingCount(None, False, False, None, None))
    calc.register(mordred.BondCount.BondCount("any", False))


def register_atom(calc: mordred.Calculator) -> None:
    """Register atom-count descriptors onto `calc`."""
    calc.register(mordred.AtomCount.AtomCount("X"))
    calc.register(mordred.AtomCount.AtomCount("HeavyAtom"))
    calc.register(mordred.Aromatic.AromaticAtomsCount)


def register_bond(calc: mordred.Calculator) -> None:
    """Register bond-count descriptors onto `calc`."""
    calc.register(mordred.HydrogenBond.HBondAcceptor)
    calc.register(mordred.HydrogenBond.HBondDonor)
    calc.register(mordred.RotatableBond.RotatableBondsCount)
    calc.register(mordred.BondCount.BondCount("any", False))
    calc.register(mordred.Aromatic.AromaticBondsCount)
    calc.register(mordred.BondCount.BondCount("heavy", False))
    calc.register(mordred.BondCount.BondCount("single", False))
    calc.register(mordred.BondCount.BondCount("double", False))
    calc.register(mordred.BondCount.BondCount("triple", False))


def register_topological(calc: mordred.Calculator) -> None:
    """Register topological descriptors onto `calc`."""
    calc1.register(mordred.McGowanVolume.McGowanVolume)
    calc1.register(mordred.TopoPSA.TopoPSA(True))
    calc1.register(mordred.TopoPSA.TopoPSA(False))
    calc1.register(mordred.MoeType.LabuteASA)
    calc1.register(mordred.Polarizability.APol)
    calc1.register(mordred.Polarizability.BPol)
    calc1.register(mordred.AcidBase.AcidicGroupCount)
    calc1.register(mordred.AcidBase.BasicGroupCount)
    calc1.register(mordred.EccentricConnectivityIndex.EccentricConnectivityIndex)
    calc1.register(mordred.TopologicalCharge.TopologicalCharge("raw", 1))
    calc1.register(mordred.TopologicalCharge.TopologicalCharge("mean", 1))


def register_index(calc: mordred.Calculator) -> None:
    """Register topological-index descriptors onto `calc`."""
    calc.register(mordred.SLogP)
    calc.register(mordred.BertzCT.BertzCT)
    calc.register(mordred.BalabanJ.BalabanJ)
    calc.register(mordred.WienerIndex.WienerIndex(True))
    calc.register(mordred.ZagrebIndex.ZagrebIndex(1, 1))
    calc.register(mordred.ABCIndex)


def register_ring(calc: mordred.Calculator) -> None:
    """Register ring-count descriptors onto `calc`."""
    calc.register(mordred.RingCount.RingCount(None, False, False, None, None))
    calc.register(mordred.RingCount.RingCount(None, False, False, None, True))
    calc.register(mordred.RingCount.RingCount(None, False, False, True, None))
    calc.register(mordred.RingCount.RingCount(None, False, False, True, True))
    calc.register(mordred.RingCount.RingCount(None, False, False, False, None))
    calc.register(mordred.RingCount.RingCount(None, False, True, None, None))


def register_estate(calc: mordred.Calculator) -> None:
    """Register E-state descriptors onto `calc`."""
    calc.register(mordred.EState)


GROUPS_BY_DESC_TYPE: dict[str, list[RegisterFn]] = {
    "best": [register_best],
    "atom": [register_atom],
    "bond": [register_bond],
    "topological": [register_topological],
    "index": [register_index],
    "ring": [register_ring],
    "estate": [register_estate],
    "all": [
        register_atom,
        register_bond,
        register_topological,
        register_index,
        register_ring,
        register_estate,
    ],
}
