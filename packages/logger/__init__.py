"""Base logger for the project

    for applaing BOM Module"""
from .logger import setup_logger

CRITICAL = 50
ERROR = 40
WARNING = 30
INFO = 20
DEBUG = 10
NOTSET = 0


def project_logger(logger_name: str, logger_level=DEBUG):
    """Logger for the project"""
    logger_obj = setup_logger(logger_name, logger_level)
    return logger_obj
