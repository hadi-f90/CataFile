#!/usr/bin/env python
"""
Test case for MyFile.py.

This test case is for testing the MyFile class.
"""
import os
from pprint import pprint
from random import choice
from sys import path

path.append('..')
import fleep
from config import pref
from lib import MyFile

SOURCE_TEST_ADDRESS = '/home/hadi/Documents/GitHub/CataFile/tests/test_cases'
DEST_TEST_ADDRESS = '/home/hadi/Documents/GitHub/CataFile/tests/test_cases/dest'
COPY_DEST = f'{DEST_TEST_ADDRESS}/copy'
MOVE_DEST = f'{DEST_TEST_ADDRESS}/move'
os.chdir(SOURCE_TEST_ADDRESS)


def populate_list_of_files(address, extension=None):
    """
    Create list of file objects from given address.

    Inpput:
    address: str or path-like object
    extension: lsit of str or None
    Returns: a list of files filter by a given extension
    """
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

# ==============MyFile Tests ====================
testcase_my_file = MyFile.MyFile(choice(files_list))
print(0, testcase_my_file)
print(1, testcase_my_file.file_name)
print(2, testcase_my_file.extension)
print(3.1, testcase_my_file.path)  # full path includes name no need 2 fullname
print(3.2, ["Fleep", "Magic", "Extension"][pref.get('file_processor')])
print(3.3, testcase_my_file.file_object.read(2048))
print(3.4, fleep.get(testcase_my_file.file_object.read(2048)))
print(4.0, testcase_my_file.fleep_detect())
print(4.1, testcase_my_file.file_info)
print(4.2, testcase_my_file.type)
print(4.3, testcase_my_file.detected_extension)
print(4.4, testcase_my_file.file_info.mime)
print(5.1, testcase_my_file.magic_detect())
print(5.2, testcase_my_file.mime)
print(5.3, testcase_my_file.type)
print(5.4, testcase_my_file.detected_extension)
print(6, testcase_my_file.file_date_time())
testcase_my_file.fleep_detect()
print(7, testcase_my_file.extension_revert())
print(8.0, testcase_my_file.copy(COPY_DEST))
print(8.2, os.path.exists(COPY_DEST + testcase_my_file.path))
print(8.3, testcase_my_file.move(MOVE_DEST))
print(8.4, os.path.exists(testcase_my_file.path))


def test_file_tester(self):
    # assert testcase_my_file.__test_archive() is True
    pass


""" @pytest.mark.parametrize("file_name", files_list)
def test_CataFile(file_name):
    print(file_name)
    my_file.CataFile(file_name) """
