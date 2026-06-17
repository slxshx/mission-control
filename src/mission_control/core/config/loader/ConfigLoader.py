import tomllib

from mission_control.core.config.errors.ConfigError import ConfigError
from mission_control.core.config.models.AppConfig import AppConfig


class ConfigLoader:
    config_path: str

    def __init__(self, config_path: str) -> None:
        self.config_path = config_path

    def load(self) -> AppConfig:
        try:
            with open(self.config_path, "rb") as file:
                data = tomllib.load(file)
        except FileNotFoundError:
            raise ConfigError(f"Config file not found: {self.config_path}")
        except tomllib.TOMLDecodeError:
            raise ConfigError(f"Invalid TOML syntax in config file: {self.config_path}")

        if "app" not in data:
            raise ConfigError("Missing required section: app")

        app_section = data["app"]

        required_fields = ["name", "version", "environment"]

        for field in required_fields:
            if field not in app_section:
                raise ConfigError(f"Missing required config value: app.{field}")

            if not app_section[field]:
                raise ConfigError(f"Config value app.{field} must not be empty")

        allowed_environments = ["development", "test", "production"]

        environment = app_section["environment"].lower()

        if environment not in allowed_environments:
            raise ConfigError(
                f"Invalid environment '{app_section['environment']}'. "
                f"Allowed values: {', '.join(allowed_environments)}"
            )

        return AppConfig(
            name=app_section["name"],
            version=app_section["version"],
            environment=environment,
        )
