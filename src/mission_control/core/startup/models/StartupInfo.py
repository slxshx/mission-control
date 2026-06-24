from dataclasses import dataclass

@dataclass()
class StartupInfo:
    app_name: str
    version: str
    environment: str
    python_version: str
    system: str
    plugins_loaded: int



