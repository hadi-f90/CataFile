from argparse import FileType
import unittest
import os
import unittest
import sys
sys.path.append('.')

from project.folders import folder
import project.logger as logger

TEST_ADDRESS = '/home/hadi/Documents/GitHub/file_categorizer/test/test_files'
new_dir = '/home/hadi/Documents/GitHub/file_categorizer/test/test_files/test2'


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
        self.folder = folder(TEST_ADDRESS)
        self.assertEqual(TEST_ADDRESS, str(self.folder))
        del self.folder
        self.countTestCases()

    # Assign non-existent folder
    def test_assiging_none_existing_folder(self):
        pass

    # Assign file
    # Check the srting representation of Assign_folder

    def test_walk_top_down(self):
        # Walker topdown
        self.f = folder(TEST_ADDRESS)
        self.assertTrue(os.path.isfile(next(self.f.walker())))

    # Walker bottom up
        self.assertTrue(os.path.isfile(next(self.f.walker(n=True))))

    def test_dir_walker(self):
        self.f = folder(TEST_ADDRESS)
        self.assertTrue(os.path.isdir(next(self.f.dir_walker())))
        self.assertTrue(os.path.isdir(next(self.f.dir_walker(n=True))))

    def test_mkdir(self):
        self.n = folder(new_dir)
        # trying to mkdir a directory
        self.n.mkdir(new_dir)
        self.assertTrue(os.path.exists(new_dir))

    def test_delete(self):
        self.n = folder(new_dir)
        self.n.delete(new_dir)
        self.assertFalse(os.path.exists(new_dir))
    # delete directory
    # delete non-existent directory


class TestDestination(unittest.TestCase):
    def Test_setFolder(self):
        pass
    # Checking Creating Destination path
    # Checking creating existing destination
    # Checking Setting destination path

    def Test_add_category(self):
        # Checking creating Categories dictionary
        pass

    def Test_folder_categories(self):
        # checking creating folder categories
        pass


if __name__ == '__main__':
    unittest.main()
