"""A Test for Folders module."""
import os
import sys

from lib.Folders import DestinationFolder

sys.path.append("..")
sys.path.append(".")

DEST_TEST_ADDRESS = "/home/hadi/Documents/GitHub/CataFile/tests/test_cases/dest/"

DEST_TEST_FOLDER = DestinationFolder()


def test_not_setting_initial_folder():
    """Test if the folder module started properly without setting folder parameter."""
    assert os.getcwd() == DEST_TEST_FOLDER.current_dir


def test_initial_category_folder_preparation():
    """Check that the initial destination folder work with init input dir."""
    assert os.path.exists(
        os.path.join(DEST_TEST_FOLDER.current_dir, "/Categories/"))


DEST_TEST_FOLDER = DestinationFolder(DEST_TEST_ADDRESS)


def test_setting_initial_folder():  # Passed
    """Test if the folder module started properly with setting folder parameter."""
    assert os.path.exists(DEST_TEST_FOLDER.current_dir)
    assert DEST_TEST_FOLDER.current_dir == DEST_TEST_ADDRESS

    # Checking creating existing destination
    # Checking Setting destination path


test_category = "Test_Category"
DEST_TEST_FOLDER.add_category(test_category)
expected_category_address = DEST_TEST_ADDRESS + test_category


def test_add_category():  # Passed
    """Test creating category dictionary."""
    assert DEST_TEST_FOLDER.category_dirs[
        test_category] == expected_category_address


def test_folder_categories():  # Passed
    """Test checking creating folder categories."""
    assert os.path.exists(expected_category_address)
