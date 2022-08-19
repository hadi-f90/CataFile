import logging
import logging.config
import sys
from datetime import datetime
from os import getcwd
from os.path import join, exists

from jalali.Jalalian import jdate
from pypref import Preferences

pref = Preferences(directory=getcwd(), filename="preferences.py")

logs_dict = {
    'save_log': True,
    'show_details': True,
    'log_file_address': '/home/hadi/Documents/GitHub/file_categorizer',
    'calendar': 'Khorsheedi',
    'log_level': 40
    }

pref.set_preferences(logs_dict)

# creating logger instance
logger = logging.getLogger(__name__)
logger.setLevel(pref.get('log_level'))

# setting calandar settings
if pref.get('calendar') == 'Khorsheedi':
    date_time = jdate('Y-m-d-H-i-s')
    log_header = 'تاریخ\t\tزمان' + '\t'*4 + 'درجه' + '\t'*2 + 'پیام\n' + '=' * 100 + '\n'
else:
    date_time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    log_header = 'Date\t\ttime' + '\t'*4 + 'level' + '\t'*2 + 'messages\n' + '='*100 + '\n'

# setting up formatter
formatter = logging.Formatter(
    f"{date_time} - %(name)s - %(levelname)s - %(message)s")

# setting up file handler if requested
if pref.get('save_log'):
    file_handler = logging.FileHandler(f"log{date_time}.log")
    file_handler.setLevel(pref.get('log_level'))
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

# setting up showing detailes if requested
if pref.get('show_details'):
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(pref.get('log_level'))
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)


logger.handlers[0].stream.write(log_header)
logger.handlers[0].stream.flush()
