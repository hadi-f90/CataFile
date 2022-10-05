"""A Test for Folders module."""
import os
import sys

from lib.Folders import Folder

sys.path.append("..")
sys.path.append(".")

TEST_ADDRESS = "/home/hadi/Documents/GitHub/CataFile/tests/test_cases"
NEW_DIR = "/home/hadi/Documents/GitHub/CataFile/tests/test_cases/test2"
DEST_TEST_ADDRESS = "/home/hadi/Documents/GitHub/CataFile/tests/test_cases/dest/"
NOT_EXISTING_ADDRESS = "/home/hadi/Documents/GitHub/CataFile/tests/test_cases/test100"


def test_not_setting_initial_folder():
    """Test if the folder module started properly without setting folder parameter."""
    folder = Folder()
    assert os.getcwd() == folder.current_dir
    del folder


'''def test_assiging_none_existing_folder():
    """Assign non-existent folder."""
    folder = Folder(NOT_EXISTING_ADDRESS)
    assert sys.stderr.readlines()[-1] == f"Message: {folder} \
        either isn't a folder or doesn't exist!"'''

# Todo: TEST Assigning file

TEST_FOLDER = Folder(TEST_ADDRESS)


def test_assigning_initial_folder():
    """Test setting initial folder parameter."""
    assert TEST_ADDRESS == TEST_FOLDER.current_dir


def test_representation():
    """Check the string representation of Assigned folder."""
    assert TEST_ADDRESS == str(TEST_FOLDER)


def test_walk_top_down():
    """Test walker method in top_down mode."""
    # Walker topdown
    assert os.path.isfile(next(TEST_FOLDER.walker()))


def test_walk_bottom_up():
    """Test walker method in bottom up mode."""
    assert os.path.isfile(next(TEST_FOLDER.walker(True)))


def test_dir_walker():
    """Test walker method."""
    assert os.path.isdir(next(TEST_FOLDER.dir_walker()))
    assert os.path.isdir(next(TEST_FOLDER.dir_walker(True)))


def test_mkdir():
    """Test to mkdir a directory."""
    TEST_FOLDER.mkdir(NEW_DIR)
    assert os.path.exists(NEW_DIR)


def test_delete():
    """Test to delete a directory."""
    TEST_FOLDER.delete(NEW_DIR)
    assert not os.path.exists(NEW_DIR)


def test_not_existing_directory_delete():
    """Test delete non-existent directory."""
    try:
        TEST_FOLDER.delete(NOT_EXISTING_ADDRESS)
        return False
    except FileNotFoundError:
        return True
