#!/usr/bin/env python

from random import choice
import pytest
import os
# from random import choice
import MyFile
from config import pref
from pprint import pprint

TEST_ADDRESS = '/home/hadi/Documents/GitHub/file_categorizer/project/test_cases'
os.chdir(TEST_ADDRESS)

files_list = [f for f in os.listdir(TEST_ADDRESS) if os.path.isfile(f)]
pprint(files_list)

testcase_MyFile = MyFile.MyFile(choice(files_list))
print(0, testcase_MyFile)
print(1, testcase_MyFile.name)
print(2, testcase_MyFile.extension)
print(3.1, testcase_MyFile.path)  # full path includes name no need to full name
print(3.2, ["Fleep", "Magic", "Extension"][pref.get('file_processor')])
# print(3.3, testcase_MyFile.file_object.read(2048))
# print(3.4, fleep.get(testcase_MyFile.file_object.read(2048)))
print(4.0, testcase_MyFile.fleep_detect())
print(4.1, testcase_MyFile.file_info)
print(4.2, testcase_MyFile.type)
print(4.3, testcase_MyFile.detected_extension)
print(4.4, testcase_MyFile.file_info.mime)
print(5.1, testcase_MyFile.magic_detect())
print(5.2, testcase_MyFile.mime)
print(5.3, testcase_MyFile.type)
print(5.4, testcase_MyFile.detected_extension)
print(6, testcase_MyFile.file_date_time())
testcase_MyFile.fleep_detect()
print(7, testcase_MyFile.extension_revert())
print(8.0, testcase_MyFile.copy('/media/hadi/iPro/test_folder_copy'))
print(8.1, testcase_MyFile.move('/media/hadi/iPro/test_folder_move'))
print(8.3, os.path.exists('/media/hadi/iPro/test_folder_move/a.ttf'))
print(8.3, os.path.exists('/media/hadi/iPro/test_folder_copy/a.ttf'))
# print(8, testcase_MyFile.check_integerity())
# testcase_MyFile.revert_font_name()
# pprint(os.listdir())

""" print('=========2ns file==========')
testcase_my_file = my_file.my_file(choice(files_list))
print(testcase_my_file.name)
print(testcase_my_file.file_info.mime)
print(testcase_my_file.path)
print(testcase_my_file.extension) """

# ==============MyFile Tests ====================


def test_file_tester(self):
    # assert testcase_MyFile.__test_archive() is True
    pass


def test_extension(self):
    pass


def test_mime_detection(self):
    pass


def test_file_path_mismatch(self):
    pass


def test_file_size(self):
    pass


def test_file_name_check(self):
    pass


""" @pytest.mark.parametrize("file_name", files_list)
def test_file_categorizer(file_name):
    print(file_name)
    my_file.file_categorizer(file_name) """
