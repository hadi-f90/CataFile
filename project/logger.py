import logging
import logging.config
import sys
from datetime import datetime
from os import getcwd
from os.path import join

from jalali.Jalalian import jdate
from pypref import Preferences

pref = Preferences(directory=getcwd(),
                   filename="preferences.py")

logs_dict = {
             'save_log': '',
             'show_details': '',
             'log_file_address': '',
             'calendar': '',
             'log_level': ''}


class logger(logging.Logger):
    def __init__(self):
        super().__init__(__name__)
        self.log = logging.getLogger('__name__')
        self.formatter = logging.Formatter(
            f"{self.set_date} - %(name)s - %(levelname)s - %(message)s")
        self.log.setLevel(pref.get('log_level'))

        if pref.get('save_log'):
            self.save_log_file()

        if pref.get('show_log_details'):
            self.show_log_details()

    def set_date(self):
        '''Sets datetime 2 Gerogian/Persian Calendar log file name & records'''
        if pref.get('calendar') == "Khorsheedi":
            self.datetime = jdate('Y-m-d-H-i-s')
        else:
            self.datetime = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

        return self.datetime

    def set_file_address(self):
        '''Returns the logging address of the log file as a path like obj'''
        return join(getcwd(), f"log {jdate('Y-m-d-H-i-s')}.log")

    def show_log_details(self):
        '''Show the details of the  log file on the screen'''
        self.stream_handler = logging.StreamHandler(stream=sys.stdout)
        self.log.addHandler(self.stream_handler)
        self.stream_handler.setFormatter()
        self.log.addHandler(self.stream_handler)

    def save_log_file(self):
        '''Prepares & saves the log file to disk'''
        self.log_file = join(getcwd, self.set_file_address())
        self.file_handler = logging.FileHandler(self.log_file)
        self.log.addHandler(self.file_handler)
        self.file_handler.setFormatter(self.formatter)
        with open(self.log_file, 'a') as self.log_file:
            self.log_file.writelines(
                '\ttime\t\tDate' + '\t'*6 + 'messages\n' + '=' * 100 + '\n')
