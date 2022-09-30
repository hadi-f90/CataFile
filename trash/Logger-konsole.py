"""works fine: A simple Logger implementation based on konsole library."""

import sys
from datetime import datetime

from jalali.Jalalian import jdate
import logging
import konsole

from preferences import preferences

sys.path.append('..')

# jdatetime.set_locale('fa_IR')
LINE = '-' * 100
DATE_TIME = jdate('Y-m-d@H:i:s') if preferences.get('calendar') else datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
# DATE_TIME2 = JalaliDateTime.now().strftime('%Y-%m-%d %H:%M:%S') if preferences.get('calendar') else datetime.now().strftime('%Y-%m-%d-%H:%M:%S')

LOG_File_NAME = f"{preferences.get('log_file_address')}/{DATE_TIME}.log"
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

Filehandler = file_handler = logging.FileHandler(LOG_File_NAME)
if preferences.get('save_log'):
    konsole._main_logger.addHandler(Filehandler)
    konsole._main_logger.handlers.append
