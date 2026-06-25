from mission_control.core.logging.enums.LogLevel import LogLevel
from rich.console import Console
from rich.text import Text

class Logger():

    console: Console

    def __init__(self, console) -> None:
        self.console = console
        

    def _log(self, label, color, message):
        level = Text(f"[{label}] ")
        level.stylize(color)
        level += message
        self.console.print(level)

    def info(self, message):
        self._log(LogLevel.INFO.label, LogLevel.INFO.color,  message)

    def success(self, message):
        self._log(LogLevel.SUCCESS.label, LogLevel.SUCCESS.color,  message)

    def warning(self, message):
        self._log(LogLevel.WARNING.label, LogLevel.WARNING.color, message)

    def error(self, message):
        self._log(LogLevel.ERROR.label, LogLevel.ERROR.color, message)

    def critical(self, message):
        self._log(LogLevel.CRITICAL.label, LogLevel.CRITICAL.color, message)

    def debug(self, message):
        self._log(LogLevel.DEBUG.label, LogLevel.DEBUG.color, message)

    def network(self, message):
        self._log(LogLevel.NETWORK.label, LogLevel.NETWORK.color, message)

    def news(self, message):
        self._log(LogLevel.NEWS.label, LogLevel.NEWS.color, message)

