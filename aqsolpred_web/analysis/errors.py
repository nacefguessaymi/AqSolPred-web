"""Prediction-error metrics for evaluating solubility models."""

from collections.abc import Sequence

import numpy as np
from loguru import logger
from sklearn.metrics import mean_absolute_error as mae
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import r2_score as r2


def get_errors(
    y_true: Sequence[float], y_pred: Sequence[float]
) -> tuple[float, float, float]:
    """Compute and print the MAE, RMSE, and R2 of a set of predictions.

    Args:
        y_true: Ground-truth target values.
        y_pred: Predicted target values, aligned by index with `y_true`.

    Returns:
        A tuple of (mae, rmse, r2).
    """
    err_mae = mae(y_true, y_pred)
    err_rmse = np.sqrt(mse(y_true, y_pred))
    err_r2 = r2(y_true, y_pred)
    logger.info(f"Ensemble MAE: {err_mae} \nRMSE: {err_rmse} \nR2: {err_r2}")
    return err_mae, err_rmse, err_r2
