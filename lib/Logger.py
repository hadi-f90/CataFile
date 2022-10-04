"""A Simple Logging Interface instead of previously defined logging methods."""

import logging
from datetime import datetime
from sys import path, stdout

from jalali.Jalalian import jdate

from preferences import preferences

path.append("..")
# path.append('.')

# creating logger instance

LINE = "-" * 100


class Logger(logging.Logger):
    """A Simple Logging Interface based on pylogger logging methods."""

    def __init__(self, name=__name__, level=logging.NOTSET):
        """
        Initialize the logger.

        :param name: The name of the logger.
        :param level: The level of the logger.
        """
        super().__init__(name, level)
        self.logger_name = name
        self.log_file_address = preferences.get("log_file_address")
        self.date_time = (jdate("Y-m-d@H:i:s") if preferences.get("calendar")
                          else datetime.now().strftime("%Y-%m-%d-%H:%M:%S"))
        self.log_file_name = f"{self.log_file_address}/log{self.date_time}.log"
        self.level = preferences.get("log_level")
        self.formatter = logging.Formatter(f"""{LINE}
{self.date_time}\n%(levelname)s\tMessage: %(message)s
Logger name:{__name__}\tfile: %(filename)s\tmodule: %(module)s\tline: %(lineno)d\tfunction: %(funcName)s"""
                                           )
        self.save_log()
        self.show_details()

    def save_log(self):
        """Save the log to a file."""
        if preferences.get("save_log"):
            self.file_handler = logging.FileHandler(self.log_file_name)
            self.file_handler.setLevel(self.level)
            self.file_handler.setFormatter(self.formatter)
            self.addHandler(self.file_handler)

    def show_details(self):
        """Show the details of the log."""
        if preferences.get("show_details"):
            self.stream_handler = logging.StreamHandler(stdout)
            self.stream_handler.setLevel(self.level)
            self.stream_handler.setFormatter(self.formatter)
            self.addHandler(self.stream_handler)

    def change_level(self, handler):
        """Change Logging leve to preference one."""
        handler.setLevel(preferences.get("log_level"))


# setting up formatter

LOGGER = Logger(__name__)
