"""AqSolPred aqueous solubility prediction pipeline.

Subpackages:
    core: shared config/constants.
    compute: Mordred-based descriptor computation.
    analysis: model evaluation/error metrics.
    cli: command-line interface (see `cli.predict`).
    web: streamlit web interface (see `web.app`).

`main.py` holds the shared prediction logic both `cli` and `web` call
into: `calculate_logS`, `predict_logS_from_descriptors`.
"""
