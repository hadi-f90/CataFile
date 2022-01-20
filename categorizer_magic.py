import os
import shutil
from sys import argv
import magic
import patoolib
from jalali.Jalalian import jdate
import regex


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
        for root, dirs, files in os.walk(self.current_dir, topdown=False):
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

        except FileExistsError or OSError():
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
        self.current_dir = os.getcwd() + '/Categories/' \
            if input_dir in ('', None) else input_dir
        # print(self.current_dir)
        if os.path.exists(self.current_dir):
            logger(msg=f'Using already existing {self.current_dir} directory.')

        else:
            os.mkdir(self.current_dir)
            logger(msg=f'Creating {self.current_dir}')

        os.chdir(self.current_dir)
        logger(msg=f'Target set to dir: {self.current_dir}')
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


# ============================== file object class ============================
class my_file():
    def __init__(self, file_object=None):
        # file type info
        self.file_object = open(file_object, 'rb')
        self.mime = magic.from_buffer(self.file_object.read(2048), mime=True)
        self.name, self.extension = os.path.splitext(file_object)
        if self.mime == '':
            self.mime = 'etc'
        print(self.mime)
        self.path = os.path.abspath(file_object)

    def file_date_time(self):
        # To-do: returns file data and time
        return (os.path.getatime(), os.path.getctime(), os.path.getmtime())

    def __test_archive(self, file=None):
        if file is None:
            file = self.path
        try:
            patoolib.test_archive(file)
            return True
        except patoolib.PatoolError:
            logger(msg='fError. {file} test Failed.')
            return False

    def check_integerity(self):
        # To do: use patoolib to check it
        if self.extension in patoolib.ArchiveFormats:
            self.__test_archive()
        # not tested for documents
        elif regex.search(r'.doc[x|m]?|.xls[x|m]?|.pp[t|s|x|m]+',
                          self.extension, flags=regex.IGNORECASE) is not None:
            test_case = shutil.copyfile(self.path, self.name+'.zip')
            result = self.__test_archive(file=test_case)
            os.remove(test_case)
            return result
        else:
            logger(msg='Not implemented integerity check!')
            return True

    def move(self, destination):
        shutil.move(self.path, destination)
        logger(msg=f'{self.path} moved to {self.mime}.')

    def __str__(self) -> str:
        return self.name


# =============== loggging mechanism ======================
def logger(*args, func=None, msg):
    global log_file
    if func:
        if len(args) > 1:
            output = str(func(args))
        elif len(args) == 1:
            output = str(func(args[0]))
        else:
            func()
    else:
        output = '-No output-'

    log = jdate('Y/m/d H:i:s') + '\t' + str(msg) + '\t' + \
        output + '\n' + '='*(len(msg) + len(output) + 25) + '\n'
    print(log)
    log_file.writelines(log)


# ==========main course====================
def main():
    print(argv[0], log_file.name)
    source_dir = folder()
    target = destination_folder()
    for _ in source_dir.walker():
        print(source_dir.selected_file_name, _, log_file.name, argv[0])
        if _ in {log_file.name, _ == argv[0]}:
            # print(_)
            continue
        # print(_)
        f = my_file(_)
        if os.path.isfile(f.path):
            if f.check_integerity():
                try:
                    print(f.mime, '\n', f.path)
                    if f.mime not in target.category_dirs.keys():
                        target.add_category(f.mime)

                    f.move(target.category_dirs[f.mime])
                except TypeError and shutil.Error:
                    logger(msg=f'An Error occured during processing {_}.\n \
                        A file with the same name may prevent moving')
                except AttributeError:
                    logger(msg=f'An Error occured during processing {_}.\n \
                        Unknown File')
            else:
                target.add_category('/Corrupted')
                f.move(target.category_dirs['/Corrupted'])
                logger(msg=f'Check {f.name} later to see what was wrong.')
    # ===== To do: Delete empty folders after moving files to categories
    # for _ in os.walk(source_dir.current_dir):
    #     if os.path. len(os.listdir(_)) < 1:
    #         try:
    #             logger(msg=f'Removing {_}')
    #             os.rmdir(_)

    #         except OSError:
    #             logger(msg=f'Error removing empty dir {_}')

    # ========= To do: Checking file integerity


if __name__ == '__main__':
    global log_file
    with open(os.path.join(
                            os.getcwd(),
                            'log' + jdate('Y-m-d-H-i-s') + '.txt'),
              'a') as log_file:

        log_file.writelines(
            ['\tDate\ttime\tmessage' + '\t'*3 + 'function output\n',
                '=' * 55, '\n'])

        main()
