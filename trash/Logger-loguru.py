"""A simple Logger implementation based on loguru library."""

import sys
from datetime import datetime

from jalali.Jalalian import jdate
from loguru import logger

from preferences import preferences

sys.path.append("..")

sys.path.append("..")

# jdatetime.set_locale('fa_IR')
LINE = "-" * 100
DATE_TIME = (jdate("Y-m-d@H:i:s") if preferences.get("calendar") else
             datetime.now().strftime("%Y-%m-%d-%H:%M:%S"))
# DATE_TIME2 = JalaliDateTime.now().strftime('%Y-%m-%d %H:%M:%S') if preferences.get('calendar') else datetime.now().strftime('%Y-%m-%d-%H:%M:%S')

LOG_File_NAME = f"{preferences.get('log_file_address')}/{DATE_TIME}.log"
FORMAT = "{time:DATE_TIME}{message}"


def setup_logger():
    """Set up LOGGER."""
    if preferences.get("show_details"):
        logger.add(sys.stdout,
                   format=FORMAT,
                   level=preferences.get("log_level"))

    if preferences.get("save_log"):
        logger.add(LOG_File_NAME,
                   format=FORMAT,
                   level=preferences.get("log_level"))


setup_logger()
logger.success("Succeeded")
