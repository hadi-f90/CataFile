"""A Test for Folders module."""
import os
import sys

import pytest

sys.path.append('..')
sys.path.append('.')
from lib.Folders import Folder

TEST_ADDRESS = '/home/hadi/Documents/GitHub/CataFile/test/test_files'
new_dir = '/home/hadi/Documents/GitHub/CataFile/test/test_files/test2'


def test_initial_folder_set():
    folder = Folder(os.getcwd()[:])
    assert os.getcwd() == folder.current_dir
    del folder


# Assign_folder
def test_assign_folder():
    folder = Folder(TEST_ADDRESS)
    assert TEST_ADDRESS == folder.current_dir


# Check the srting representation of Assign_folder
def test_representation():
    folder = Folder(TEST_ADDRESS)
    assert TEST_ADDRESS == str(folder)
    del folder


# Assign non-existent folder
def test_assiging_none_existing_folder():
    pass

# Assign file
# Check the srting representation of Assign_folder


def test_walk_top_down():
    # Walker topdown
    f = Folder(TEST_ADDRESS)
    assert os.path.isfile(next(f.walker()))

    # Walker bottom up
    assert os.path.isfile(next(f.walker(n=True)))


def test_dir_walker():
    f = Folder(TEST_ADDRESS)
    assert os.path.isdir(next(f.dir_walker()))
    assert os.path.isdir(next(f.dir_walker(n=True)))


def test_mkdir():
    n = Folder(new_dir)
    # trying to mkdir a directory
    n.mkdir(new_dir)
    assert os.path.exists(new_dir)


def test_delete():
    n = Folder(new_dir)
    n.delete(new_dir)
    assert not os.path.exists(new_dir)
    # delete directory
    # delete non-existent directory


# TestDestination Folder
def test_set_folder():
    pass
    # Checking Creating Destination path
    # Checking creating existing destination
    # Checking Setting destination path


def test_add_category():
    # Checking creating Categories dictionary
    pass


def test_folder_categories():
    # checking creating folder categories
    pass
