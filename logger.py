import logging

class Logger:
    """
    A simple logger class for logging messages.
    """

    def __init__(self, name: str) -> None:
        """
        Initializes the Logger with a specified name.
        
        :param name: The name of the logger.
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def debug(self, message: str) -> None:
        """
        Logs a message with level DEBUG.
        
        :param message: The message to log.
        """
        self.logger.debug(message)

    def info(self, message: str) -> None:
        """
        Logs a message with level INFO.
        
        :param message: The message to log.
        """
        self.logger.info(message)

    def warning(self, message: str) -> None:
        """
        Logs a message with level WARNING.
        
        :param message: The message to log.
        """
        self.logger.warning(message)

    def error(self, message: str) -> None:
        """
        Logs a message with level ERROR.
        
        :param message: The message to log.
        """
        self.logger.error(message)

    def critical(self, message: str) -> None:
        """
        Logs a message with level CRITICAL.
        
        :param message: The message to log.
        """
        self.logger.critical(message)