from typing import Optional

class ClickerError(Exception):
    """Base class for exceptions in the autoclicker module."""
    pass

class ConfigurationError(ClickerError):
    """Raised when there is a configuration issue."""
    def __init__(self, message: str, config_key: Optional[str] = None) -> None:
        super().__init__(message)
        self.config_key = config_key

class ClickRateExceededError(ClickerError):
    """Raised when the click rate exceeds a specified limit."""
    def __init__(self, limit: int, rate: int) -> None:
        super().__init__(f'Click rate {rate} exceeds limit of {limit}.')
        self.limit = limit
        self.rate = rate

class ClickerNotActiveError(ClickerError):
    """Raised when trying to perform actions on a non-active clicker."""
    def __init__(self) -> None:
        super().__init__('The clicker is not currently active.')

class InvalidClickTargetError(ClickerError):
    """Raised when the target for a click is invalid."""
    def __init__(self, target: str) -> None:
        super().__init__(f'Invalid target: {target}')
        self.target = target
