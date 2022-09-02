#!/usr/bin/env python

import pytest
import os
from random import choice
import MyFile as MyFile


TEST_ADDRESS = '/home/hadi/Documents/GitHub/file_categorizer/project/test_cases'
# os.chroot(TEST_ADDRESS)
os.chdir(TEST_ADDRESS)

files_list = [f for f in os.listdir(TEST_ADDRESS) if os.path.isfile(f)]
print(files_list)

testcase_MyFile = MyFile.MyFile('a.ttf')
print(1, testcase_MyFile.name)
print(2, testcase_MyFile.extension)
print(3, testcase_MyFile.mime)
print(4, testcase_MyFile.path)  # full path includes name no need to full name
print(5, testcase_MyFile)
print(6, testcase_MyFile.file_date_time())
print(7, testcase_MyFile.test_archive())
print(8, testcase_MyFile.check_integerity())
testcase_MyFile.revert_font_name()
print(os.listdir())

""" print('=========2ns file==========')
testcase_my_file = my_file.my_file(choice(files_list))
print(testcase_my_file.name)
print(testcase_my_file.file_info.mime)
print(testcase_my_file.path)
print(testcase_my_file.extension) """

# ==============MyFile Tests ====================


def test_file_tester(self):
    assert testcase_MyFile.__test_archive() == True


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
