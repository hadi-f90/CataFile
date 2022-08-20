from os import getcwd
from pypref import Preferences

# =============preferences setting=================
pref = Preferences(directory=getcwd(),
                   filename="preferences.py")

default_options_dict = {
    'source_dir': getcwd(),
    'destination_dir': getcwd(),
    'file_processor': 'magic',
    'save_log': True,
    'show_details': True,
    'log_file_address': getcwd(),
    'calendar': 'Khorsheedi',
    'log_level': 10
    }

pref.set_preferences(default_options_dict)
