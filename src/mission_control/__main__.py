from mission_control.core.config.errors.ConfigError import ConfigError
from mission_control.core.config.loader.ConfigLoader import ConfigLoader
from mission_control.core.startup.services.StartupService import StartupService


BANNER = r"""
  __  __ ___ ____ ____ ___ ___  _   _    ____ ___  _   _ _____ ____   ___  _     
 |  \/  |_ _/ ___/ ___|_ _/ _ \| \ | |  / ___/ _ \| \ | |_   _|  _ \ / _ \| |    
 | |\/| || |\___ \___ \| | | | |  \| | | |  | | | |  \| | | | | |_) | | | | |    
 | |  | || | ___) |__) | | |_| | |\  | | |__| |_| | |\  | | | |  _ <| |_| | |___ 
 |_|  |_|___|____/____/___\___/|_| \_|  \____\___/|_| \_| |_| |_| \_\\___/|_____|

         ___   _   ___  
 __   __/ _ \ / | / _ \ 
 \ \ / / | | || || | | |
  \ V /| |_| || || |_| |
   \_/  \___(_)_(_)___/ 

  ___       _ _   _       _ _     _                             _                           
 |_ _|_ __ (_) |_(_) __ _| (_)___(_)_ __   __ _   ___ _   _ ___| |_ ___ _ __ ___  ___       
  | || '_ \| | __| |/ _` | | |_  / | '_ \ / _` | / __| | | / __| __/ _ \ '_ ` _ \/ __|      
  | || | | | | |_| | (_| | | |/ /| | | | | (_| | \__ \ |_| \__ \ ||  __/ | | | | \__ \_ _ _ 
 |___|_| |_|_|\__|_|\__,_|_|_/___|_|_| |_|\__, | |___/\__, |___/\__\___|_| |_| |_|___(_|_|_)
                                          |___/       |___/                                 
"""


def main() -> None:
    print(BANNER)

    try:
        config_loader = ConfigLoader("config/config.toml")
        app_config = config_loader.load()

        startup_service = StartupService()
        startup_info = startup_service.build_startup_info(app_config)

    except ConfigError as error:
        print("[ERROR] Failed to load configuration")
        print(error)
        return

    print("[✓] Configuration loaded")
    print("[✓] Startup information collected")
    print()
    print(f"Name: {startup_info.app_name}")
    print(f"Version: {startup_info.version}")
    print(f"Environment: {startup_info.environment}")
    print(f"Python: {startup_info.python_version}")
    print(f"System: {startup_info.system}")
    print(f"Plugins loaded: {startup_info.plugins_loaded}")
    print()
    print("Mission Control ready.")


if __name__ == "__main__":
    main()
