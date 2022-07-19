import font_rename
import os
import magic
import patoolib
import regex
import shutil
from logger import logger


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
        self.name_revert()

    def file_date_time(self):
        # To-do: returns file data and time
        return (os.path.getatime(), os.path.getctime(), os.path.getmtime())

    def __test_archive(self, file=None):
        if file is None:
            file = self.path
        try:
            patoolib.test_archive(file)
            return True
        except:
            logger(msg='fError. {file} test Failed.')
            return False

    def check_integerity(self):
        # To do: use patoolib to check it
        if self.extension in patoolib.ArchiveFormats:
            self.__test_archive()
        # not tested for documents
        elif regex.search(r'.doc[x|m]?|.xls[x|m]?|.pp[t|s|x|m]+',
                          self.extension, flags=regex.IGNORECASE) is not None:
            test_case = shutil.copyfile(self.path, f'{self.name}.zip')
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

    def name_revert(self):  # not testes Yet!
        if regex.search(r'[tow]*tf2?',
                        self.extension, flags=regex.IGNORECASE) is not None:
            number = 0
            while os.path.exists(self.name+str(number)+self.extension):
                number += 1
            try:
                font_rename.rename_font(self.path)

            except FileExistsError:
                logger(msg=f'An Error occured processing file {self.path}')

            finally:
                logger(msg=f'Font name reverted to it original name:\
                       {self.name}')
