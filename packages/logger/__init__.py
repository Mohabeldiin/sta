"""Base logger for the project

    for applaing BOM Module"""
from .logger import setup_logger, get_parser

CRITICAL = 50
ERROR = 40
WARNING = 30
INFO = 20
DEBUG = 10
NOTSET = 0


def project_logger(logger_name: str, logger_level=DEBUG):
    """Logger for the project

    Args:
        logger_name (str): name of the logger
        logger_level (int, optional): level of the logger. Defaults to DEBUG.

    Returns:
        logger: logger object."""
    logger_obj = setup_logger(logger_name, logger_level)
    return logger_obj

__all__ = ["project_logger", "setup_logger", "get_parser"]
