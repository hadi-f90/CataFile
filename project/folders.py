

# =============directory definitions=================
class folder:
    def __init__(self,
                 current_directory=os.path.dirname(os.path.abspath(__file__))):
        # Get the directory name where the current running Python file resides
        # src: https://www.devdungeon.com/
        # Setting and checking the directory
        self.current_dir = current_directory
        logger(msg=f'Current dir is set to: {self.current_dir}')

        try:
            assert os.path.isdir(self.current_dir)
        except AssertionError:
            logger(msg=f'{self.current_dir} is not a directory. Check it!')

    # Appending path to file/folder name function
    def walker(self, n=False,):
        """Walks through directory to return
        append the full adrress to each file

        Yields:
            [str]: [full path of file]
        """
        for root, dirs, files in os.walk(self.current_dir, topdown=False):
            if len(files) != 0:
                for _ in files:
                    self.selected_file_name = _
                    yield os.path.join(root, _)

        if n is True:
            self.walker()

    def dir_walker(self, n=False):
        """Walks through directory to return
        append the full adrress to each file

        Yields:
            [str]: [full path of file]
        """
        for root, dirs, files in os.walk(self.current_dir, topdown=n):
            if len(files) != 0:
                for _ in dirs:
                    self.selected_dir_name = _
                    yield os.path.join(root, _)

    def mkdir(self, sub_dir):
        """Creates a series of directorys from a given list/tuple/set"""
        try:
            logger(sub_dir,
                   func=os.makedirs,
                   msg=f'Creating {self.current_dir} if does not exist...')

        except OSError:
            logger(msg=f'Using it the existing {sub_dir} directory...')

    def delete(self, sub_dir):
        try:
            assert os.path.isdir(sub_dir)
            logger(sub_dir, os.remove, f'{sub_dir} removed.')

        except AssertionError:
            logger(f'{sub_dir} was not a directory')

    def __str__(self) -> str:
        return self.current_dir


class destination_folder(folder):
    def __init__(self,
                 input_dir=input(
                     f'Enter the destination folder for the categories.\n \
                     deffault:{os.getcwd()}:')):
        super().__init__()
        global logger
        # preparing destination path
        # self.mkdir(os.getcwd()+'/Categories/')
        self.current_dir = f'{os.getcwd()} /Categories/' \
            if input_dir in ('', None) else input_dir
        # print(self.current_dir)
        if os.path.exists(self.current_dir):
            logger(msg=f'Using already existing {self.current_dir} directory.')

        else:
            os.mkdir(self.current_dir)
            logger(msg=f'Creating {self.current_dir}')

        os.chdir(self.current_dir)
        logger(msg=f'destination set to dir: {self.current_dir}')
        # print(self.current_dir)

        self.category_dirs = {}
        # print(self.category_dirs)

    def add_category(self, category_name):
        self.category_dirs[category_name] = \
            self.current_dir + category_name
        # print(self.category_dirs)
        if os.path.exists(self.category_dirs[category_name]):
            logger(
                msg=f'Using the existing {self.category_dirs[category_name]}'
                )
        else:
            self.mkdir(self.category_dirs[category_name])
            logger(msg=f'{category_name} directory structure created.')

    def __dict__(self):
        return self.category_dirs
