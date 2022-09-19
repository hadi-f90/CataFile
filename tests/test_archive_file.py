"""Testing for MyFile.py."""
import os
import sys
from pprint import pprint
from random import choice

from lib import MyFile

sys.dont_write_bytecode = True

SOURCE_TEST_ADDRESS = '/home/hadi/Documents/GitHub/file_categorizer/project/test_cases'
# DEST_TEST_ADDRESS = '/home/hadi/Documents/GitHub/file_categorizer/project/test_cases/dest'
os.chdir(SOURCE_TEST_ADDRESS)


def populate_list_of_files(address, extensions=()):
    """Create a list of files based on given list of extensions.

    extension must have a dot 
    This function takes a directory address
    and returns a list of files filter by a given extension.
    """
    list_of_files = []

    if extensions == ():
        list_of_files.extend(_ for _ in os.listdir(address)
                             if os.path.isfile(_))
    else:
        for _ in extensions:
            if not _.startswith('.'):
                _ = f'.{_}'  # totally buggy
        list_of_files.extend(
            _ for _ in os.listdir(address)
            if os.path.isfile(_) and os.path.splitext(_)[-1] in extensions)

    return list_of_files


print('=========Testing Archive File Class==========')

files_list = populate_list_of_files(SOURCE_TEST_ADDRESS,
                                    ('.zip', '.apk', '.rar', '.7z', '.docx'))
pprint(files_list)

testcase_my_file = MyFile.ArchiveFile(choice(files_list))
print(testcase_my_file)
print(testcase_my_file.file_info.mime)
# print(testcase_my_file.path)
# print(testcase_my_file.extension)
# print(8, testcase_MyFile.check_integerity())
