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


print("=========Testing Font Class==========")
files_list = populate_list_of_files(SOURCE_TEST_ADDRESS, (".woff"))
pprint(files_list)
testcase_MyFile = MyFile.FontFile(choice(files_list))
print(0, testcase_MyFile)
print(1, testcase_MyFile.font_name)
print(1.1, testcase_MyFile.file_name)
print(2, testcase_MyFile.extension)
print(3.1, testcase_MyFile.path)  # full path
# testcase_MyFile.rename('cbc.ttf')
testcase_MyFile.revert_font_name()
files_list = populate_list_of_files(SOURCE_TEST_ADDRESS, (".woff2"))
pprint(files_list)
print(4, testcase_MyFile.file_name)
files_list = populate_list_of_files(SOURCE_TEST_ADDRESS, )
pprint(files_list)