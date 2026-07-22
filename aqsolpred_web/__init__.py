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

__version__ = "0.0.0"

import os
import sys
from ast import literal_eval
from typing import Any

from loguru import logger

from .predict import calculate_logs

__all__ = [calculate_logs]

logger.disable("aqsolpred_web")

LOG_FORMAT = (
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSSZ}</green> | "
    "<level>{level: <8}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
)


def enable_logging(
    level_set: int,
    stdout_set: bool = True,
    file_path: str | None = None,
    log_format: str = LOG_FORMAT,
) -> None:
    r"""Enable logging.

    Args:
        level: Requested log level: `10` is debug, `20` is info.
        file_path: Also write logs to files here.
    """
    config: dict[str, Any] = {"handlers": []}
    if stdout_set:
        config["handlers"].append(
            {
                "sink": sys.stdout,
                "level": level_set,
                "format": log_format,
                "colorize": True,
            }
        )
    if isinstance(file_path, str):
        config["handlers"].append(
            {"sink": file_path, "level": level_set, "format": log_format}
        )
    # https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.configure
    logger.configure(**config)

    logger.enable("aqsolpred_web")


if literal_eval(os.environ.get("AQSOLPRED_WEB_LOG", "False")):
    level = int(os.environ.get("AQSOLPRED_WEB_LOG_LEVEL", 20))
    stdout = literal_eval(os.environ.get("AQSOLPRED_WEB_STDOUT", "True"))
    log_file_path = os.environ.get("AQSOLPRED_WEB_LOG_FILE_PATH", None)
    enable_logging(level, stdout, log_file_path)
