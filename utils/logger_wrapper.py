import logging
from utils.json_logger_formatter import JSONFormatter

class LoggerWrapper:
    def __init__(self, name: str):
        # To reduce verbosity you may suppress logging messages from flet_core module
        logging.getLogger("flet_core").setLevel(logging.INFO)
        
        self.logger = logging.getLogger(name)
        handler = logging.StreamHandler()
        handler.setFormatter(JSONFormatter())
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.DEBUG)

    def debug(self, message: dict):
        self.logger.debug(message)

    def info(self, message: dict):
        self.logger.info(message)

    def warning(self, message: dict):
        self.logger.warning(message)

    def error(self, message: dict):
        self.logger.error(message)

    def critical(self, message: dict):
        self.logger.critical(message)
