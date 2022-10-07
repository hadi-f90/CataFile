import os
import sys
from pprint import pprint
from random import choice

from config import pref
from lib.File import MyFile

sys.path.append("..")
sys.path.append(".")

SOURCE_TEST_ADDRESS = "/home/hadi/Documents/GitHub/CataFile/project/test_cases"
DEST_TEST_ADDRESS = "/home/hadi/Documents/GitHub/CataFile/project/test_cases/dest"
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
testcase_my_file = MyFile.FontFile(choice(files_list))
print(0, testcase_my_file)
print(1, testcase_my_file.font_name)
print(1.1, testcase_my_file.file_name)
print(2, testcase_my_file.extension)
print(3.1, testcase_my_file.path)  # full path
# testcase_my_file.rename('cbc.ttf')
testcase_my_file.revert_font_name()
files_list = populate_list_of_files(SOURCE_TEST_ADDRESS, (".woff2"))
pprint(files_list)
print(4, testcase_my_file.file_name)
files_list = populate_list_of_files(SOURCE_TEST_ADDRESS, )
pprint(files_list)
