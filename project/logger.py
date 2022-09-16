import logging
from datetime import datetime
from sys import stdout

from config import pref
from jalali.Jalalian import jdate

# creating logger instance
logger = logging.getLogger(__name__)
date_time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
line = "-" * 100
# setting up formatter
formatter = logging.Formatter(
    f"{line}\n{date_time}:\nfile: %(filename)s\nmodule: %(module)s\nline: %(lineno)d\nfunction: %(funcName)s\n%(levelname)s - %(message)s\n"
)


# setting calandar settings
def set_calendar():
    global date_time
    if pref.get("calendar") == "Khorsheedi":
        date_time = jdate("Y-m-d-H-i-s")


# setting up file handler if requested
def save_log():
    if pref.get("save_log"):
        file_handler = logging.FileHandler(f"log{date_time}.log")
        file_handler.setLevel(pref.get("log_level"))
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)


# setting up showing detailes if requested
def show_details():
    if pref.get("show_details"):
        stream_handler = logging.StreamHandler(stdout)
        stream_handler.setLevel(pref.get("log_level"))
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)


def change_level():
    logger.setLevel(pref.get("log_level"))


def setup_logger():
    set_calendar()
    change_level()
    save_log()
    show_details()


print(pref.get("save_log"), pref.get("show_details"))
print(logger.handlers)
