# config: utf-8
import logging.config

from main_app import LOGGER_CONFIG_PATH


logging.config.fileConfig(LOGGER_CONFIG_PATH)
logger = logging.getLogger("main_app")
