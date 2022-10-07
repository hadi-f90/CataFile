"""
A set of classes that are used to manipulate folder structures.

The Folder class is the main class that is used to manipulate folder
"""

import os

from lib.Logger import LOGGER


# =============directory definitions=================
class Folder:
    """initial variables: .

    current_directory: set to current working directory if not set
    """

    def __init__(self, current_directory=os.getcwd()[:]):
        """Initiate Folder module.

        Args:
            current_directory: Defaults to os.getcwd().
        """
        # Setting and checking the directory
        self.current_dir = current_directory

        LOGGER.info("Trying to set address to:%s", self.current_dir)
        if not os.path.isdir(self.current_dir):
            LOGGER.critical("%s either isn't a folder or doesn't exist!",
                            self.current_dir)

    # Appending path to file/folder name function
    def walker(
        self,
        top_down=False,
    ):
        """Walk through dir to return append the full adrress to each file.

        Yields:
            [str]: [full path of file]
        """
        for folder_data in os.walk(
                self.current_dir, topdown=top_down
        ):  # Changed root, dirs, files ==> folder_data tuple
            if len(folder_data[-1]) > 0:
                for _ in folder_data[-1]:
                    # Todo: why not to use os.path.abspath here?
                    # Todo: A good to use glob.iglob('**', recursive=True)
                    # Todo: Do use pathlib
                    self.selected_file_name = _
                    yield os.path.join(folder_data[0], _)

        if top_down is True:
            self.walker()

    def dir_walker(self, top_down=False):
        """Walk through dir to return append the full adrress to each folder.

        Yields:
            [str]: [full path of file]
        """
        for root, dirs, files in os.walk(self.current_dir, topdown=top_down):
            if len(files) != 0:
                for _ in dirs:
                    self.selected_dir_name = _
                    yield os.path.join(root, _)

    def mkdir(self, sub_dir):
        """Create a series of directories from a given list/tuple/set."""
        try:
            LOGGER.info("Creating %s if not exist...", self.current_dir)
            os.makedirs(sub_dir)

        except OSError:
            LOGGER.info("Using existing %s directory...", sub_dir)

    def delete(self, sub_dir):
        """Delete a series of directories from a given list/tuple/set."""
        try:
            LOGGER.info("Checking %s if exists...", sub_dir)
            assert os.path.exists(sub_dir)
            LOGGER.warning("Removing %s...", sub_dir)
            os.rmdir(sub_dir)
            LOGGER.info("%s Removed successfully!", sub_dir)

        except AssertionError:
            LOGGER.warning("%s was not a directory.", sub_dir)

        except FileNotFoundError:
            LOGGER.warning("%s was not found.", sub_dir)

    def __str__(self) -> str:
        """Return the name of current dir."""
        return self.current_dir

    def __repr__(self) -> str:
        """Return the name of current dir."""
        return self.current_dir


class DestinationFolder(Folder):
    """Create a destination_folder_label based on Folder Class.

    Args:
        Folder (_type_): _description_
    """

    def __init__(self, input_dir=os.getcwd()):
        """Get a folder name, If not set, os.getcwd() is default.

        Args:
            input_dir (_type_, optional): Defaults to os.getcwd().
        """
        super().__init__()
        # preparing destination path
        # self.mkdir(os.getcwd()+'/Categories/')
        self.current_dir = (f"{os.getcwd()}/Categories/"
                            if input_dir in ("", None) else input_dir)
        if os.path.exists(self.current_dir):
            LOGGER.info("Using existing directory:%s", self.current_dir)

        else:
            os.mkdir(self.current_dir)
            LOGGER.info("Creating %s", self.current_dir)

        os.chdir(self.current_dir)
        LOGGER.info("destination set to dir:%s", self.current_dir)

        self.category_dirs = {}

    def add_category(self, category_name):
        """Add a missing file to the destination folder.

        Args:
            category_name (_type_): _description_
        """
        self.category_dirs[category_name] = self.current_dir + category_name
        if os.path.exists(self.category_dirs[category_name]):
            LOGGER.info("Using existing %s", self.category_dirs[category_name])
        else:
            self.mkdir(self.category_dirs[category_name])
            LOGGER.info("%s directory structure created.", category_name)
