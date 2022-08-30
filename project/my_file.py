import os
import shutil

import font_rename
import magic
import patoolib
import regex

from logger import logger
import fleep


# ============================== file object class ============================
class MyFile():
    def __init__(self, file_object=None):
        # file type info
        self.file_object = open(file_object, 'rb')
        self.mime = magic.from_buffer(self.file_object.read(2048), mime=True)
        self.name, self.extension = os.path.splitext(file_object)
        if self.mime == '':
            self.mime = 'etc'
        # print(self.mime)
        self.path = os.path.abspath(file_object)
        self.name_revert()

    def file_date_time(self):
        # To-do: returns file data and time
        return (os.path.getatime(self.path),
                os.path.getctime(self.path),
                os.path.getmtime(self.path))

    def test_archive(self):
        try:
            patoolib.test_archive(self.path)
            logger.debug(f'Testing file {self.path}')
            return True
        except patoolib.util.PatoolError as e:
            logger.error(f'Error. Testing {self.path} Failed with error {str(e)}')
            return False

    def check_integerity(self):
        if self.extension in patoolib.ArchiveFormats:
            self.__test_archive()
        # not tested for documents & apks
        elif regex.search(r'.doc[x|m]?|.xls[x|m]?|.pp[t|s|x|m]+ .od[b|c|f|g|m|p|t|s]+ .ap[k|x]+', self.extension, flags=regex.IGNORECASE) is not None:
            test_case = shutil.copyfile(self.path, f'{self.name}.zip')
            print(os.path.abspath(test_case))
            result = self.__test_archive(file=test_case)
            os.remove(test_case)
            return result
        else:
            logger.debug('Integerity check not implemented for it ! Skipping')
            return True

    def move(self, destination):
        shutil.move(self.path, destination)
        logger.info(f'{self.path} moved to {self.mime}.')

    def __str__(self) -> str:
        return self.path

    def name_revert(self):  # not testes Yet!
        # if the file type is not known thentry fo file its type
        if self.extension is None:
            self.fleep_info = fleep.get(self.file_object.read(2048))
            new_extension = self.fleep_info.mime.split('/')[-1]
            if new_extension is not None:
                os.rename(self.full_name,
                          self.path + self.name + new_extension)
        # if it is a font file
        elif regex.search(r'[tow]*tf2?',
                          self.extension,
                          flags=regex.IGNORECASE) is not None:
            number = 0
            while os.path.exists(self.name+str(number)+self.extension):
                number += 1
                try:
                    font_rename.rename_font(self.path)

                except FileExistsError:
                    logger.error(f'An Error occured renaming {self.path}')

                finally:
                    logger.info(
                        f'Font reverted to its original name: {self.name}')


class my_file():
    def __init__(self, file_object=None):
        self.file_object = open(file_object, 'rb')
        self.file_info = fleep.get(self.file_object.read(2048))
        self.name, self.extension = os.path.splitext(file_object)
        if len(self.file_info.mime) < 1:
            self.mime = 'etc'
        elif self.extension in ('.txt', '.py'):
            self.mime = 'text/plain'
        else:
            self.file_info.mime[0]
        self.path = os.path.abspath(file_object)

    def file_date_time(self):
        '''returns file data and time'''
        return (os.path.getatime(), os.path.getctime(), os.path.getmtime())

    def check_integerity(self):
        logger(msg='Not implemented integerity check!')

    def move(self, destination):
        shutil.move(self.path, destination)
        logger(msg=f'{self.path} moved to {destination}.')

    def __str__(self) -> str:
        return self.name


class FontFile(MyFile):
    pass


class ArchiveFile(MyFile):
    pass


class DocumentFile(MyFile):
    pass


class MediaFile(MyFile):
    pass
