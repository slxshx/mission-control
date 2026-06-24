from mission_control.core.config.models.AppConfig import AppConfig
from mission_control.core.startup.models.StartupInfo import StartupInfo
import sys
import platform as plat

class StartupService:
    def build_startup_info(self, app_config: AppConfig) -> StartupInfo:
        python_version = sys.version
        system = f"{plat.system()} - {plat.release()}"
        return StartupInfo(app_config.name, app_config.version, app_config.environment, python_version, system, plugins_loaded=0)  
    
