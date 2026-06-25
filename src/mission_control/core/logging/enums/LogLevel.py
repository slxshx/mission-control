from enum import Enum

class LogLevel(Enum):
    INFO = "INFO", "white"
    NEWS = "NEWS", "cyan"
    NETWORK = "NETWORK", "bright_blue"
    WARNING = "WARNING", "dark_orange3"
    ERROR = "ERROR", "red3"
    CRITICAL = "CRITICAL", "deep_pink3"
    DEBUG = "DEBUG", "bright_black"
    SUCCESS = "SUCCESS", "bright_green"

    def __init__(self, label, color) -> None:
        self.label = label
        self.color = color
        


