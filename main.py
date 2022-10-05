"""The main function that will be called when Start() is called."""

import os
import shutil
from sys import argv

from config import pref
from lib.Folders import DestinationFolder, Folder
from lib.Logger import LOGGER, setup_logger
from lib.MyFile import MyFile

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
    SOURCE = Folder(pref.get("source_dir"))
    DESTINATION = DestinationFolder(pref.get("destination_dir"))
    setup_logger()
    LOGGER.debug(argv[0], LOGGER.handlers[0])
    for _ in SOURCE.walker():
        LOGGER.debug(f"file to be processed: {SOURCE.selected_file_name}")
        process_file(_)
        continue

    empty_folder_delete()


def process_file(_):
    """Detect given file & move to its category folder."""
    f = MyFile(_)

    if os.path.isfile(f.path):  # Todo: removed f.check_integerity():
        try:
            LOGGER.debug(f.mime, "\n", f.path)
            if f.mime not in DESTINATION.category_dirs:
                DESTINATION.add_category(f.mime)
            f.move(DESTINATION.category_dirs[f.mime])

        except (TypeError, shutil.Error):
            LOGGER.critical(f"Error during processing {_}.\n \
                    A file with the same name may have prevented it from \
                        being moved")

        except AttributeError:
            LOGGER.critical(
                f"Error during processing{_}. File type isn't known.")

        DESTINATION.add_category("/Corrupted")
        try:
            f.move(DESTINATION.category_dirs["/Corrupted"])

        except shutil.Error:
            LOGGER.critical(
                f"Error copying {str(f)}. Maybe because of duplicate name")
        finally:
            LOGGER.critical(
                f"An error occured processing {str(f)}. Check it manually!")


def empty_folder_delete():
    """Delete empty folders."""
    # ===== To do: Delete empty folders after moving files to categories
    for _ in os.walk(SOURCE.current_dir):
        if len(os.listdir(_)) < 1:
            try:
                LOGGER.warning(f"Removing {_}")
                os.rmdir(_)

            except OSError:
                LOGGER.critical(f"Error removing empty dir {_}")
