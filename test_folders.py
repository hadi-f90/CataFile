import unittest
import os


from project.folders import folder


class TestFolders(unittest.TestCase):
    def test_initial_folder_set(self):
        self.folder = folder(os.getcwd()[:])
        print(os.getcwd(), self.folder)
        self.assertEqual(os.getcwd(), self.folder.current_dir)
        del self.folder
    # Assign_folder

    def Assign_folder(self):
        self.folder('/home/hadi/Documents/GitHub/file_categorizer/test_cases')
    # Assign non-existent folder
    # Assign file
    # Check the return value of Assign_folder
    # Check the srting representation of Assign_folder

    def walk(self):
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
