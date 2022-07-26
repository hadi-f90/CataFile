import os
import shutil
from sys import argv

from jalali.Jalalian import jdate

import logger
from folders import destination_folder, folder
from my_file import MyFile

from . import tui

# ==========main course====================
SOURCE = folder()
DESTINATION = destination_folder()


def main():
    print(argv[0], logger.LOG_FILE.name)
    for _ in SOURCE.walker():
        print(SOURCE.selected_file_name, _, logger.LOG_FILE.name, argv[0])
        # if the sellected file is the current app , then forget about it
        # To d: now that I have multiple app files, I need change itP
        if _ in {logger.LOG_FILE.name, _ == argv[0]}:
            # print(_)
            continue
        # print(_)
        else:
            process_file(_)

    empty_folder_delete()


def process_file(_):
    f = MyFile(_)

    if os.path.isfile(f.path) and f.check_integerity():
        try:
            print(f.mime, '\n', f.path)
            if f.mime not in DESTINATION.category_dirs.keys():
                DESTINATION.add_category(f.mime)
            f.move(DESTINATION.category_dirs[f.mime])

        except (TypeError, shutil.Error):
            logger.log.critical(f'An Error occured during processing {_}.\n \
                    A file with the same name may have prevented it from \
                        being moved')

        except AttributeError:
            logger.log.critical(f'An Error occured during processing {_}.\n \
                    Unknown File')

        DESTINATION.add_category('/Corrupted')
        try:
            f.move(DESTINATION.category_dirs['/Corrupted'])

        except shutil.Error:
            logger.log.critical(f'There was an error copying {f.name}. \
                    This can be the result of an exising file with the \
                        same name.')
        finally:
            logger.log.critical(f'The  file has integeritiy errors.\
                    Check {f.name} later to see what was wrong.')


def empty_folder_delete():
    # ===== To do: Delete empty folders after moving files to categories
    for _ in os.walk(SOURCE.current_dir):
        if len(os.listdir(_)) < 1:
            try:
                logger.log.warning(f'Removing {_}')
                os.rmdir(_)

            except OSError:
                logger.log.critical(f'Error removing empty dir {_}')


if __name__ == '__main__':

    main()
