from colorama import Fore
import logging

from enum import Enum

class LogDefinitions(Enum):
    MESSAGE = 0
    DEBUG = 1
    SUCCESS = 2
    INFO = 3
    WARNING = 4
    ERROR = 5
    CRITICAL = 6

class Logger:
    instance = None

    def __init__(self):
        self.setup()

    def setup(self):
        logging.basicConfig(filename="logs.log", filemode="w", level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s',datefmt='%Y-%m-%d %H:%M:%S')

    @staticmethod
    def get_instance():
        """ Get the instance of the logger and create a new if doesn't exist
        Return Logger.instance : instance of the logger
        """
        if Logger.instance is None:
            Logger.instance = Logger()
        return Logger.instance
    
    def log(self, definition, message):
        match definition:
            case LogDefinitions.MESSAGE:
                print(f"{Fore.MAGENTA}-> {message} {Fore.RESET}")
            case LogDefinitions.DEBUG:
                print(f"{Fore.MAGENTA}DEBUG: {message} {Fore.RESET}")
            case LogDefinitions.SUCCESS:
                print(f"{Fore.GREEN}SUCCESS: {message} {Fore.RESET}")
                logging.info(f"Successfully {message}")
            case LogDefinitions.INFO:
                print(f"{Fore.BLUE}INFO: {message} {Fore.RESET}")
                logging.info(message)
            case LogDefinitions.WARNING:
                print(f"{Fore.YELLOW}WARNING: {message} {Fore.RESET}")
                logging.warning(message)
            case LogDefinitions.ERROR:
                print(f"{Fore.LIGHTRED_EX}ERROR: {message} {Fore.RESET}")
                logging.error(message)
            case LogDefinitions.CRITICAL:
                print(f"{Fore.RED}CRITICAL: {message} {Fore.RESET}")
                logging.critical(message)
                
if __name__ == "__main__":
    Logger.get_instance().log(definition=LogDefinitions.DEBUG, message="message")
    Logger.get_instance().log(definition=LogDefinitions.SUCCESS, message="message")
    Logger.get_instance().log(definition=LogDefinitions.INFO, message="message")
    Logger.get_instance().log(definition=LogDefinitions.WARNING, message="message")
    Logger.get_instance().log(definition=LogDefinitions.ERROR, message="message")
    Logger.get_instance().log(definition=LogDefinitions.CRITICAL, message="message")