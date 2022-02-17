
import numbers
import os
import shutil
from sys import argv, flags
from jalali.Jalalian import jdate

from my_file import my_file
from folders import folder, destination_folder
from logger import logger

# ==========main course====================


def main():
    print(argv[0], log_file.name)
    source_dir = folder()
    target = destination_folder()
    for _ in source_dir.walker():
        print(source_dir.selected_file_name, _, log_file.name, argv[0])
        if _ in {log_file.name, _ == argv[0]}:
            # print(_)
            continue
        # print(_)
        f = my_file(_)
        if os.path.isfile(f.path):
            if f.check_integerity():
                try:
                    print(f.mime, '\n', f.path)
                    if f.mime not in target.category_dirs.keys():
                        target.add_category(f.mime)

                    f.move(target.category_dirs[f.mime])
                except TypeError and shutil.Error:
                    logger(msg=f'An Error occured during processing {_}.\n \
                        A file with the same name may prevent moving')
                except AttributeError:
                    logger(msg=f'An Error occured during processing {_}.\n \
                        Unknown File')
            else:
                target.add_category('/Corrupted')
                try:
                    f.move(target.category_dirs['/Corrupted'])

                except shutil.Error:
                    logger(msg=f'There was an error copying {f.name}. \
                        This can be the result of a file with the same name.')
                finally:
                    logger(msg=f'The  file has integeritiy errors.\
                        Check {f.name} later to see what was wrong.')
    # ===== To do: Delete empty folders after moving files to categories
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
