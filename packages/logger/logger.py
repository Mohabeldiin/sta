"""Python Base Logger that i integrate with my python scripts

    for more information refer to https://github.com/Mohabeldiin/python_base_logger

    Attributes:
        LEVEL (int): The level of logging to use
        FILENAME (str): The name of the file to log to
        FILEMODE (str): The mode to open the file in
        FORMAT (str): The format of the log
        DATEFMT (str): The format of the date

    Returns:
        logging.Logger: logger"""
import logging

FORMAT = '%(asctime)s - %(name)s - %(levelname)s: %(message)s'
DATEFMT = '%Y-%m-%d %H:%M:%S'
LEVEL = logging.INFO
FILEMODE = "w"
FILENAME = None


def setup_logger(
    logger_name,
    logger_level=LEVEL,
    logger_filename=FILENAME,
    logger_filemode=FILEMODE
):
    """Sets Up the logger
            Log Example:
                2022-05-24 00:45:56,230 - Logger Name - INFO: Message
            Returns:
                logging.Logger: logger"""
    logging.basicConfig(
        format=FORMAT,
        datefmt=DATEFMT,
        level=logger_level,
        filename=logger_filename,
        filemode=logger_filemode)
    return logging.getLogger(logger_name)
