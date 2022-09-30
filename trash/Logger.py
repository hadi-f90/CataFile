"""A Simple Logging Interface instead of previously defined logging methods."""

import logging
from datetime import datetime
from sys import stdout

from sys import path
from jalali.Jalalian import jdate

path.append('..')
# path.append('.')

from preferences import preferences

# creating logger instance

LINE = '-' * 100
DATE_TIME = jdate('%Y-%m-%d-%H:%M:%S') if preferences.get('calendar') else datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
FORMATTER = logging.Formatter(
    f"""
    {LINE}
    Logger name:{__name__}
    {DATE_TIME}:
    file: %(filename)s
    module: %(module)s
    line: %(lineno)d
    function: %(funcName)s
    %(levelname)s - %(message)s""")


class logger(logging.Logger):
    """A Simple Logging Interface based on pylogger logging methods."""

    def __init__(self, name = __name__ , level=logging.NOTSET):
        """
        Initialize the logger.

        :param name: The name of the logger.
        :param level: The level of the logger.
        """
        super().__init__(name, level)
        self.logger_name = name
        self.log_file_address = preferences.get('log_file_address')
        self.log_file_name = f'{self.log_file_name}_{self.date_time}.log'
        logging.Formatter(FORMATTER)
        self.set_calendar()
        self.save_log()
        self.show_details()

    def set_calendar(self):
        """Set the calendar to the one defined in  prefereneces."""
        if preferences.get('calendar') == 'Khorsheedi':
            self.date_time = jdate('Y-m-d-H-i-s')

        else:
            self.date_time = jdate(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))

    def save_log(self):
        """Save the log to a file."""
        if preferences.get('save_log'):
            self.file_handler = logging.FileHandler(self.log_file_address + self.log_file_name)
            self.file_handler.setLevel(preferences.get('log_level'))
            self.file_handler.setFormatter(FORMATTER)
            self.addHandler(self.file_handler)

    def show_details(self):
        """Show the details of the log."""
        if preferences.get('show_details'):
            self.stream_handler = logging.StreamHandler(stdout)
            self.stream_handler.setLevel(preferences.get('log_level'))
            self.stream_handler.setFormatter(FORMATTER)
            self.addHandler(self.stream_handler)

    def change_level(self, handler):
        """Change Logging leve to preference one."""
        handler.setLevel(preferences.get('log_level'))


# setting up formatter


LOGGGER = logger(__name__)
