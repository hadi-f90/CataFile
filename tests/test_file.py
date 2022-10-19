#!/usr/bin/env python
"""Test cases for File class in File.py."""
import os
from pathlib import PurePath
from random import choice
from sys import path

import fleep
import magic

from config import pref
from lib import File

path.append("..")
path.append(".")

path.append("..")

SOURCE_TEST_ADDRESS = "/home/hadi/Documents/GitHub/CataFile/tests/test_cases"
DEST_TEST_ADDRESS = "/home/hadi/Documents/GitHub/CataFile/tests/test_cases/dest"
COPY_DEST = f"{DEST_TEST_ADDRESS}/copy"
MOVE_DEST = f"{DEST_TEST_ADDRESS}/move"
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

# ==============MyFile Tests ====================
c = choice(files_list)
testcase_file = File.File(c)


def test_file_init():  # Passed!
    """Check initializing test file module."""
    assert isinstance(testcase_file, File.File)


def test_get_file_name():  # passed!
    """Check file name representation."""
    assert testcase_file.full_file_name == c


def test_get_file_extension():  # Passed!
    """Check file extension."""
    extension = c[c.index("."):]
    assert extension == testcase_file.extension


# print(
#    testcase_file.parent_dir,
#    PurePath("/home/hadi/Documents/GitHub/test center/CataFile/test_cases"))


def test_get_parent_folder(
):  # Fails: Todo:In logs, returns only 1 dot! why & how?!
    """Check parent folder representation."""
    assert testcase_file.parent_dir == PurePath(
        "/home/hadi/Documents/GitHub/test center/CataFile/test_cases"
    )  # full path includes name no need 2 fullname


def test_get_full_file_name():
    """Verifiy full name variable data."""
    assert testcase_file.full_file_name == c


def test_reading_file_header():  # Passed!
    """Verify reading header."""
    assert testcase_file.file_header == testcase_file.file_object.read(2048)


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
r = open(c, "rb")
info = fleep.get(r.read(2048))
testcase_file.fleep_detect()


def test_file_mime_detection_with_fleep():  # Failed to pass!
    """Verifiy fleep file detection function."""
    assert info.mime[0] == testcase_file.mime


def test_file_type():
    """Check file type variable."""
    assert info.type[0] == testcase_file.type


def test_file_detection_function_extension():
    """Check file extension detecting function."""
    ext = testcase_file.extension[:]
    assert ext == testcase_file.detected_extension


# ================maigc module test=====================
testcase_file.magic_detect()


def test_file_detection_with_magic():  # Todo write tests here
    """Check magic lib file detection facility."""
    testcase_file.mime
    testcase_file.type


def test_reverting_file_extension_function():  # It seems that passed
    """Verifiy extension revert functionality."""
    ext = testcase_file.extension[:]
    testcase_file.extension_revert()
    assert ext == testcase_file.extension


def test_file_copy_function():
    """Check if file copy function is available."""
    testcase_file.copy(COPY_DEST)
    os.path.exists(testcase_file.full_path)


def test_move_function():
    # Has problems with not existing dirs, same is true about copy function
    """Check that move function works correctly."""
    testcase_file.move(MOVE_DEST)
    assert os.path.exists(testcase_file.full_path)


def test_file_tester():
    """Haven't decided to test file_tester.

    assert testcase_my_file.__test_archive() is True.
    """


r.close()
""" @pytest.mark.parametrize("file_name", files_list)
def test_CataFile(file_name):
    print(file_name)
    my_file.CataFile(file_name) """
