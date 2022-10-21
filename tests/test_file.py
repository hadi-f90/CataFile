#!/usr/bin/env python
"""Test cases for File class in File.py."""
import os
from glob import glob
from pathlib import Path
from random import choice
from sys import path

path.append('..')
path.append('.')
import fleep
import magic
from config import pref
from lib import File, Logger


SOURCE_TEST_ADDRESS = "/home/hadi/Documents/GitHub/CataFile/tests/test_cases"
DEST_TEST_ADDRESS = "/home/hadi/Documents/GitHub/CataFile/tests/test_cases/dest"
COPY_DEST = f"{DEST_TEST_ADDRESS}/copy"
MOVE_DEST = f"{DEST_TEST_ADDRESS}/move"
os.chdir(SOURCE_TEST_ADDRESS)


def populate_list_of_files(address, extension=None):
    """Create list of file objects from given address.

    Input:
    address: str or path-like object
    extension: lsit of str or None
    Returns: a list of files filter by a given extension
    """
    if extension is not None:
        return glob(f'*.{extension}')

    return [x for x in Path(address).iterdir() if x.is_file()]


# ==============MyFile Tests ====================
c = choice(populate_list_of_files(SOURCE_TEST_ADDRESS))
f = open(c, 'rb')
f_data = f.read(128)

testcase_file = File.File(c)


def test_file_init():  # Passed!
    """Check initializing test file module."""
    assert isinstance(testcase_file, File.File)


def test_get_file_name():  # passed!
    """Check file name representation."""
    assert testcase_file.full_file_name == c.name


def test_get_file_extension():  # Passed!
    """Check file extension."""
    assert c.suffix == testcase_file.extension


def test_get_full_file_name(): # Passed!
    """Verifiy full name variable data."""
    assert testcase_file.full_file_name == c.name


def test_get_parent_folder():  # Passed!
    """Check parent folder representation."""
    assert testcase_file.parent_dir == Path(SOURCE_TEST_ADDRESS)  # full path includes name no need 2 fullname


def test_reading_file_header():  # Passed!
    """Verify reading header."""
    assert testcase_file.file_header == f_data


""" def test_file_date_time_function():  # passed just in py3.8 & py3.9 
    ""Verify read file date function works.""
    assert (
        testcase_file.file_date_time() == os.path.getatime(
            testcase_file.full_path),
        os.path.getctime(testcase_file.full_path),
        os.path.getmtime(testcase_file.full_path),
    ) """


# ================fleep_detect tests======================
# print(3.2, ["Fleep", "Magic", "Extension"][pref.get("file_processor")])

info = fleep.get(f_data)
testcase_file.fleep_detect()


def test_fleep_mime_detection():  # Passed!
    """Verifiy fleep file detection function."""
    assert info.mime[0] == testcase_file.mime


def test_fleep_file_type_detection():  # Failed!
    """Check file type variable."""
    assert info.type[0] == testcase_file.type


def test_fleep_extension_detection():  # Failed!
    """Check file extension detecting function."""
    assert f'.{info.extension[0]}' == testcase_file.detected_extension


# ================maigc module test=====================
testcase_file.magic_detect()


def test_magic_mime_detection():  # Seemingly passed...
    """Check magic lib file detection facility."""
    assert testcase_file.mime == magic.from_buffer(f_data, mime=True)


def test_magic_type_detection():  # Failed
    """Detect file type using magic type detection function."""
    assert testcase_file.type == magic.from_buffer(f_data)


def test_magic_extension_detection():
    """Detect file extension using magic type detection function."""


def test_reverting_file_extension_function():  # Failed due 2 type detection problem
    """Verifiy extension revert functionality."""
    ext = testcase_file.extension[:]
    testcase_file.extension_revert()
    assert ext == testcase_file.extension


def test_file_copy_function():  # Passed!
    """Check if file copy function is available."""
    testcase_file.copy(COPY_DEST)
    os.path.exists(testcase_file.full_path)


def test_move_function():  # It seems that it's passed but logs show wrong addresses
    # Has problems with not existing dirs, same is true about copy function
    """Check that move function works correctly."""
    testcase_file.move(MOVE_DEST)
    assert os.path.exists(testcase_file.full_path)


def test_file_tester():
    """Haven't decided to test file_tester.

    assert testcase_my_file.__test_archive() is True.
    """


f.close()
""" @pytest.mark.parametrize("file_name", files_list)
def test_CataFile(file_name):
    print(file_name)
    my_file.CataFile(file_name) """
