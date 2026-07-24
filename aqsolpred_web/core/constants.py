"""Project-wide constants for the AqSolPred prediction pipeline.

Scoped to the pipeline itself — as opposed to
`compute.constants`, which is scoped
to descriptor computation (`SELECTED_COLUMNS`).
"""

from __future__ import annotations

from pathlib import Path
from urllib.request import urlretrieve
from loguru import logger

# Model files are downloaded on first use into a local cache dir and reused
# after that, rather than shipped inside the installed package.
DEFAULT_MODELS_DIR = Path.home() / ".cache" / "aqsolpred_web" / "models"

# Original model weights, from Sorkun's upstream repo (this project is a
# fork of it). Cite [1, 2] per README when using predictions from these.
MODELS_BASE_URL = "https://raw.githubusercontent.com/mcsorkun/AqSolPred-web/main"
MLP_MODEL_FILENAME = "aqsolpred_mlp_model.pkl"
XGB_MODEL_FILENAME = "aqsolpred_xgb_model.pkl"


def ensure_model_file(filename: str, models_dir: Path = DEFAULT_MODELS_DIR) -> Path:
    """Return a local path to a pretrained model file, downloading it first
    if it isn't already cached.

    Args:
        filename: Model filename, e.g. MLP_MODEL_FILENAME or
            XGB_MODEL_FILENAME.
        models_dir: Local directory to cache downloaded files in. Created
            if it doesn't already exist.

    Returns:
        Path to the local model file, guaranteed to exist on return.
    """
    models_dir.mkdir(parents=True, exist_ok=True)
    local_path = models_dir / filename

    if not local_path.exists():
        logger.debug(
            f"Model {filename} is not existing. Downloading {filename} to cached path at {local_path}"
        )
        urlretrieve(f"{MODELS_BASE_URL}/{filename}", local_path)
    return local_path
