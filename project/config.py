from os import getcwd
from pypref import Preferences
from logger import logger
# =============preferences setting=================
pref = Preferences(directory=getcwd(),
                   filename="preferences.py")

file_processing_dict = {
    'source_dir': '',
    'destination_dir': '',
    'file_processor': 'magic'}

pref.set_preferences(file_processing_dict)

if pref.get('save_log') or pref.get('show_details'):
    new_log = logger()
