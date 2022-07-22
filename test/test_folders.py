import unittest
import os
import unittest
import sys
sys.path.append('.')

from project.folders import folder
import project.logger as logger

TEST_ADDRESS = '/home/hadi/Documents/GitHub/file_categorizer/test'


class TestFolders(unittest.TestCase):
    def test_initial_folder_set(self):
        self.folder = folder(os.getcwd()[:])
        self.assertEqual(os.getcwd(), self.folder.current_dir)
        self.countTestCases()
        del self.folder

    # Assign_folder
    def test_Assign_folder(self):
        self.folder = folder(TEST_ADDRESS)
        self.assertEqual(TEST_ADDRESS, self.folder.current_dir)
        self.countTestCases()

    # Check the srting representation of Assign_folder
    def test_representation(self):
        self.assertEqual(TEST_ADDRESS, self.folder)
        del self.folder
        self.countTestCases()

    # Assign non-existent folder
    def test_assiging_none_existing_folder(self):
        pass

    # Assign file
    # Check the srting representation of Assign_folder

    def test_walk(self):
        pass
    # Walker topdown
    # Walker bottom up

    def dir_walker(self):
        pass

    def mkdir(self):
        pass
    # trying to mkdir a directory
    # trying to make an existing directory

    def delete(self):
        pass
    # delete file
    # delete directory
    # delete non-existent directory


""" class TestDestination(unittest.TestCase):
    def setFolder(self):
        pass
    # Checking Creating Destination path
    # Checking creating existing destination
    # Checking Setting destination path

    def add_category(self):
        # Checking creating Categories dictionary
        pass

    def folder_categories(self):
        # checking creating folder categories
        pass
 """

if __name__ == '__main__':
    unittest.main()
