import logging
from logging.handlers import RotatingFileHandler

# Constants for the logger
LOG_FILE = 'app.log'
MAX_BYTES = 5 * 1024 * 1024  # 5 MB
BACKUP_COUNT = 3

def setup_logger():
    # Create a logger
    logger = logging.getLogger('AppLogger')
    logger.setLevel(logging.DEBUG)

    # Create a rotating file handler
    handler = RotatingFileHandler(LOG_FILE, maxBytes=MAX_BYTES, backupCount=BACKUP_COUNT)
    handler.setLevel(logging.DEBUG)

    # Create a formatter and set it for the handler
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)
    return logger

# Example usage if this is run as a script
if __name__ == '__main__':
    logger = setup_logger()
    logger.info('Logger setup complete.')