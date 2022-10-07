"""The main function that will be called when Start() is called."""

import os
import shutil
from sys import argv

from config import pref
from lib.Folders import DestinationFolder, Folder
from lib.Logger import LOGGER
from lib.File import MyFile

# ==========main course====================
SOURCE = None
DESTINATION = None


def main():
    """Process each file found in folders.

    Set the source & destination directories based on preferences
    then process files found in the directory tree.
    Finally omit the empty directories.
    """
    global SOURCE, DESTINATION
    SOURCE = Folder(pref.get('source_dir'))
    DESTINATION = DestinationFolder(pref.get('destination_dir'))
    LOGGER.debug(argv[0], LOGGER.handlers[0])
    for _ in SOURCE.walker():
        LOGGER.debug('file to be processed: %s', SOURCE.selected_file_name)
        process_file(_)
        # continue

    empty_folder_delete()


def process_file(_):
    """Detect given file & move to its category folder."""
    f = MyFile(_)

    if os.path.isfile(f.path):  # Todo: removed f.check_integerity():
        try:
            LOGGER.debug(f.mime, '\n', f.path)
            if f.mime not in DESTINATION.category_dirs:
                DESTINATION.add_category(f.mime)
            f.move(DESTINATION.category_dirs[f.mime])

        except (TypeError, shutil.Error):
            LOGGER.critical('Error during processing %s.\n \
                    A file with the same name may have prevented it from \
                        being moved', _)

        except AttributeError:
            LOGGER.critical(
                "Error during processing %s. File type isn't known.", _)

        DESTINATION.add_category('/Corrupted')
        try:
            f.move(DESTINATION.category_dirs['/Corrupted'])

        except shutil.Error:
            LOGGER.critical(
                'Error copying %s. Maybe because of duplicate name', str(f))
        finally:
            LOGGER.critical(
                'An error occured processing %s. Check it manually!', str(f))


def empty_folder_delete():
    """Delete empty folders."""
    # ===== To do: Delete empty folders after moving files to categories
    for _ in os.walk(SOURCE.current_dir):
        if len(os.listdir(_)) < 1:
            try:
                LOGGER.warning('Removing %s', _)
                os.rmdir(_)

            except OSError:
                LOGGER.critical('Error removing empty dir %s', _)
