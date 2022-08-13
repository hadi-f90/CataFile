import logging.config
from pypref import Preferences
from os import getcwd
logging_config = {
    'disable_existing_loggers': False,
    'version': 1,
    'formatters': {
        'short': {
            'format': '%(asctime)s %(levelname)s %(name)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'formatter': 'short',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'ERROR',
        },
        'plugins': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False
        }
    },
}

logging.config.dictConfig(logging_config)

pref = Preferences(directory=getcwd(),
                   filename="preferences.py")


options_dict = {
    'source_dir': '',
    'destination_dir': '',
    'file_processor': 'magic',
    'save_log': '',
    'show_details': '',
    'log_file_address': '',
    'calendar': '',
    'log_level': ''}


pref.set_preferences(options_dict)
