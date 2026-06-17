import tomllib
from mission_control.core.config.models.AppConfig import AppConfig
from mission_control.core.config.errors.ConfigError import ConfigError

class ConfigLoader:
    config_path: str

    def __init__(self, configPath: str) -> None:
        self.config_path = configPath

    def load(self):
        try:
            with open(self.config_path,"rb") as f:
                data = tomllib.load(f)
        except: 
            raise ConfigError("Couldn't find config path, check path variable.")
        
            
        app_section = data["app"]
                        

        return AppConfig(
            name = app_section["name"],
            version = app_section["version"],
            environment = app_section["environment"])

