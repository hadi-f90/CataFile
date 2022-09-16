import os
from pprint import pprint
from random import choice

import MyFile
import pytest
from config import pref

SOURCE_TEST_ADDRESS = "/home/hadi/Documents/GitHub/file_categorizer/project/test_cases"
DEST_TEST_ADDRESS = (
    "/home/hadi/Documents/GitHub/file_categorizer/project/test_cases/dest")
COPY_DEST = f"{DEST_TEST_ADDRESS}/copy"
MOVE_DEST = f"{DEST_TEST_ADDRESS}/move"
os.chdir(SOURCE_TEST_ADDRESS)


def populate_list_of_files(address, extension=None):
    """This function takes a directory address
    and returns a list of files filter by a given extension"""
    list_of_files = []

    if extension is None:
        list_of_files.extend(_ for _ in os.listdir(address)
                             if os.path.isfile(_))
    else:
        list_of_files.extend(_ for _ in os.listdir(address)
                             if os.path.isfile(_) and _.endswith(extension))

    return list_of_files


files_list = populate_list_of_files(SOURCE_TEST_ADDRESS)
pprint(files_list)

print("=========Testing Archive File Class==========")
# testcase_my_file = my_file.my_file(choice(files_list))
# print(testcase_my_file.file_info.mime)
# print(testcase_my_file.path)
# print(testcase_my_file.extension)
# print(8, testcase_MyFile.check_integerity())
