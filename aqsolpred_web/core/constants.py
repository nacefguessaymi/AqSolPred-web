"""Project-wide constants for the AqSolPred prediction pipeline.

Scoped to the pipeline itself — as opposed to
`compute.constants`, which is scoped
to descriptor computation (`SELECTED_COLUMNS`).
"""

from pathlib import Path

# Repo layout is:
#   aqsolpred-web/   <- this file's directory (the code root)
#   models/          <- sibling directory holding the pkl files
# Computed relative to this file rather than hardcoded, so it's correct
# no matter where the repo is checked out or mounted.
DEFAULT_MODELS_DIR = Path(__file__).resolve().parent.parent.parent / "models"

# Pretrained model filenames, expected inside the directory passed as
# `models_dir` to function.py / app.py.

MLP_MODEL_FILENAME = "aqsolpred_mlp_model.pkl"
XGB_MODEL_FILENAME = "aqsolpred_xgb_model.pkl"
