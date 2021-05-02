import os


CONFIGS_DIR = 'configs'
LOGGER_CONFIG_FILE = 'logger.ini'

CONFIGS_PATH = os.path.join(os.path.dirname(__file__), CONFIGS_DIR)
LOGGER_CONFIG_PATH = os.path.join(CONFIGS_PATH, LOGGER_CONFIG_FILE)
