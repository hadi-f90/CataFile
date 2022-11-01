#!/usr/bin/env python
"""Test cases for File class in File.py."""
import os
from glob import glob
from pathlib import Path
from random import choice
from sys import path
import defity
import magic
import fleep
import puremagic
import filetype
import pyfsig

path.append('..')
path.append('.')
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
f_data = f.read(2048)

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


# def test_reading_file_header():  # Passed!
    """Verify reading header."""
#     assert testcase_file.file_header == f_data


# ================== Magic File Detect Test ======================
info = magic.from_buffer(f_data, mime=True)
file_type, extension = info.split('/')
testcase_file.magic_detect()


def test_magic_detect_extension():
    """Detect file extension using magic lib."""
    assert testcase_file.detected_extension == extension


def test_magic_detect_type():
    """Detect file type using magic lib."""
    assert testcase_file.type == file_type


# ================fleep module test=====================
info = fleep.get(f_data)
file_type = info.type
extension = info.extension[0]
testcase_file.fleep_detect()


def test_fleep_detect_extension():
    assert testcase_file.detected_extension == extension


def test_fleep_detect_type():
    assert testcase_file.type == file_type


# ================Pure Magic module test=====================
info = puremagic.magic_file(c)
testcase_file.pure_magic_detect()


def test_pure_magic_detect():  # Failed
    print(info)
    assert testcase_file.pure_magic_detect()[0][2] == info.split('/')[1]


# ================Defity module test=====================
info = defity.from_file(c)
mime, extension = info.split('/')
testcase_file.defity_detect()


def test_defity_type_detect():
    """Verify Defity Detected file type correctly."""
    assert testcase_file.type == info


def test_defity_extension_detect():
    """Verity defity detected extension of file correctly."""
    assert str(testcase_file.detected_extension) in extension


# ================filetype module test=====================
testcase_file.filetype_detect()


def test_filetype_extension_detect():
    assert testcase_file.detected_extension == filetype.guess_extension(c)


def test_filetype_type_detect():
    assert testcase_file.type == filetype.guess_mime(c)
# ================pyfisig module test=====================


def test_pyfsig_detect():
    assert testcase_file.pyfsig_detect() == pyfsig.get_from_path(c)

# ============ other functions ======================
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


f.close()

