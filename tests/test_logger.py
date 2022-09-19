"""Logging mechanism test cases."""
from sys import path

from lib import logger

import preferences as pref

path.append("..")

test_logger = logger.LOGGGER

test_logger.name = "testing logger"
print("name", test_logger.name, "\n" * 4, test_logger.level, test_logger.log)
test_logger.level = 0
test_logger.info("This is info level log")
test_logger.debug("This is debug level log")
test_logger.warning("This is warning level log")
test_logger.error("This is error level log")
test_logger.critical("This is critical level log")
print(pref.preferences.get("save_log"), pref.preferences.get("show_details"))
print(test_logger.handlers)
