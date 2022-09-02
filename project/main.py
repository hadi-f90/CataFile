import os
import shutil
from sys import argv

from config import pref
from folders import destination_folder, folder
from logger import logger, setup_logger
from MyFile import MyFile

# ==========main course====================
SOURCE = None
DESTINATION = None


def main():
    global SOURCE, DESTINATION
    SOURCE = folder(pref.get('source_dir'))
    DESTINATION = destination_folder(pref.get('destination_dir'))
    setup_logger()
    logger.debug(argv[0], logger.handlers[0])
    for _ in SOURCE.walker():
        logger.debug(f'file to be processed: {SOURCE.selected_file_name}')
        process_file(_)
        continue

    empty_folder_delete()


def process_file(_):
    f = MyFile(_)

    if os.path.isfile(f.path) and f.check_integerity():
        try:
            logger.debug(f.mime, '\n', f.path)
            if f.mime not in DESTINATION.category_dirs:
                DESTINATION.add_category(f.mime)
            f.move(DESTINATION.category_dirs[f.mime])

        except (TypeError, shutil.Error):
            logger.critical(f'Error during processing {_}.\n \
                    A file with the same name may have prevented it from \
                        being moved')

        except AttributeError:
            logger.critical(
                f"Error during processing{_}. File type isn't known.")

        DESTINATION.add_category('/Corrupted')
        try:
            f.move(DESTINATION.category_dirs['/Corrupted'])

        except shutil.Error:
            logger.critical(
                f'Error copying {str(f)}. Maybe because of duplicate name')
        finally:
            logger.critical(f'It seems that an error occured while processing {str(f)}. Check it manually!')


def empty_folder_delete():
    # ===== To do: Delete empty folders after moving files to categories
    for _ in os.walk(SOURCE.current_dir):
        if len(os.listdir(_)) < 1:
            try:
                logger.warning(f'Removing {_}')
                os.rmdir(_)

            except OSError:
                logger.critical(f'Error removing empty dir {_}')
