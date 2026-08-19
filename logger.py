import logging
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='app.log', max_bytes=5*1024*1024, backup_count=3):
    """
    Set up a rotating logger that writes logs to a specified file.

    Parameters:
    log_file (str): The name of the log file.
    max_bytes (int): The maximum file size before rotation.
    backup_count (int): The maximum number of backup files to keep.
    """
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # Log all levels of messages

    # Create a rotating file handler
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add handler to logger
    logger.addHandler(handler)

    return logger