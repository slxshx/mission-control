from dataclasses import dataclass

@dataclass
class AppConfig:
    """"AppConfig that holds the current system"""
    name: str
    version: str
    environment: str



