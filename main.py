import os
import shutil
from sys import argv

from jalali.Jalalian import jdate

from folders import destination_folder, folder
from logger import logger
from my_file import my_file

from . import ui


# ==========main course====================

def main():
    print(argv[0], log_file.name)
    source_dir = folder()
    destination = destination_folder()

    for _ in source_dir.walker():
        print(source_dir.selected_file_name, _, log_file.name, argv[0])
        # if the sellected file is the current app , then forget about it & continue the rest
        # To d: now that I have multiple app files, I need change it
        if _ in {log_file.name, _ == argv[0]}:
            # print(_)
            continue
        # print(_)
        f = my_file(_)

        if os.path.isfile(f.path):
            if f.check_integerity():
                try:
                    print(f.mime, '\n', f.path)
                    if f.mime not in destination.category_dirs.keys():
                        destination.add_category(f.mime)
                    f.move(destination.category_dirs[f.mime])

                except (TypeError, shutil.Error):
                    logger(msg=f'An Error occured during processing {_}.\n \
                        A file with the same name may have prevented it from \
                            being moved')

                except AttributeError:
                    logger(msg=f'An Error occured during processing {_}.\n \
                        Unknown File')
            else:
                destination.add_category('/Corrupted')
                try:
                    f.move(destination.category_dirs['/Corrupted'])

                except shutil.Error:
                    logger(msg=f'There was an error copying {f.name}. \
                        This can be the result of an exising file with the \
                            same name.')
                finally:
                    logger(msg=f'The  file has integeritiy errors.\
                        Check {f.name} later to see what was wrong.')


def empty_folder_delete():
    pass  # ===== To do: Delete empty folders after moving files to categories
    # for _ in os.walk(source_dir.current_dir):
    #     if os.path. len(os.listdir(_)) < 1:
    #         try:
    #             logger(msg=f'Removing {_}')
    #             os.rmdir(_)

    #         except OSError:
    #             logger(msg=f'Error removing empty dir {_}')


if __name__ == '__main__':

    global log_file
    with open(os.path.join(
                            os.getcwd(),
                            'log' + jdate('Y-m-d-H-i-s') + '.txt'),
              'a') as log_file:

        log_file.writelines(
            ['\tDate\ttime\tmessage' + '\t'*3 + 'function output\n',
                '=' * 55, '\n'])

        main()
