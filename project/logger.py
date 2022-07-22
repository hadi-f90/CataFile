import logging
import os
import sys
from jalali.Jalalian import jdate

LOG_FILE = os.path.join(os.getcwd(), 'log' + jdate('Y-m-d-H-i-s') + '.log')

log = logging.getLogger('__name__')
log.setLevel(logging.INFO)
file_handler = logging.FileHandler(LOG_FILE)
stream_handler = logging.StreamHandler(stream=sys.stdout)
formatter = logging.Formatter(f"{jdate('Y-m-d-H-i-s')} - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
log.addHandler(file_handler)
log.addHandler(stream_handler)
