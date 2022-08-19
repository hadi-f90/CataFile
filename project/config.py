from os import getcwd
from pypref import Preferences

# =============preferences setting=================
pref = Preferences(directory=getcwd(),
                   filename="preferences.py")

options_dict = {
    'source_dir': '',
    'destination_dir': '',
    'file_processor': 'magic',
    'save_log': True,
    'show_details': True,
    'log_file_address': '/home/hadi/Documents/GitHub/file_categorizer',
    'calendar': 'Khorsheedi',
    'log_level': 10
    }

pref.set_preferences(options_dict)
