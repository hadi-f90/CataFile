import os
import shutil

import fleep
import magic
import patoolib
import regex
from fontbro import Font

from config import pref
from logger import logger


def create_proper_file_instance():
    '''tryies to detect file type and creates an instance of it
    based on its mime type
    Gets:
        A file_object
    Returns:
        None'''
    pass


# ============================== file object class ============================
class MyFile():
    def __init__(self, file_object=None):
        # file type info
        self.file_object = open(file_object, 'rb')
        self.path = os.path.abspath(file_object)
        self.name, self.extension = os.path.splitext(self.path)
        self.file_header = self.file_object.read(2048)
        if pref.get('file_processor') == 0:
            self.fleep_detect()

        elif pref.get('file_processor') == 1:
            self.mime = self.extension = self.magic_detect()

        elif pref.get('file_processor') == 2:
            self.mime = self.extension

        else:
            logger.error('file_processor not set')
        # self.extension_revert()

    def magic_detect(self):
        '''Detects file type using magic module'''
        self.mime = magic.from_buffer(self.file_header, mime=True)
        self.type, self.detected_extension = self.mime.split('/')
        if self.mime == ('', None):
            self.mime = 'etc'

    def fleep_detect(self):
        '''Detects file type using fleep module'''
        self.file_info = fleep.get(self.file_header)
        self.type = self.file_info.type[0]
        self.detected_extension = self.file_info.extension[0]
        self.mime = self.file_info.mime
        self.mime = 'etc' if len(self.mime) < 1 else self.file_info.mime[0]

    def file_date_time(self):
        # To-do: returns file data and time
        return (os.path.getatime(self.path),
                os.path.getctime(self.path),
                os.path.getmtime(self.path))

    def move(self, destination):
        shutil.move(self.path, destination)
        logger.info(f'{self.path} moved to {self.mime}.')

    def copy(self, destination):
        shutil.copy(self.path, destination)
        logger.info(f'{self.path} copied to {destination}')

    def extension_revert(self):
        # if the file type is not known then try fo file its type
        if self.extension in (None, '') or self.detected_extension != self.extension:
            logger.info(f'Changing {self.path} extension to {self.detected_extension}')
            new_name = f'{self.name}.{self.detected_extension}'
            os.rename(self.path, new_name)
            self.extension = self.detected_extension
            self.path = os.path.abspath(new_name)

    def __str__(self) -> str:
        return self.path


class FontFile(MyFile, Font):
    def __init__(self, file_object=None):
        super().__init__(file_object)
        self.font = Font(file_object)
        self.extension = self.font.get_format()
        self.name = self.font.get_name(key=Font.NAME_FAMILY_NAME)
        self.version = self.font.get_version()
        self.weight = self.font.get_weight()

        self.revert_font_name()

    def revert_font_name(self):  # not testes Yet!
        try:
            self.font.rename()
            logger.info(f'Font reverted to its original name: {self.name}')

        except FileExistsError as e:
            logger.error(f'Error {e} prevented it from renaming {self.path}.\
                Another File with the same name already exists.\
                Trying Numbering...')
            number = 0
            new_font_name = f'{self.name}{self.version}{number}.{self.extension}'
            while os.path.exists(new_font_name):
                number += 1
                new_font_name = f'{self.name}{self.version}({number}).{self.extension}'

            self.font.rename(new_font_name)
            logger.info(f'{self.name} renamed to {new_font_name}')
            self.name = self.font.get_name(key=Font.NAME_FAMILY_NAME)


class ArchiveFile(MyFile):
    def __init__(self, file_object=None):
        super().__init__(file_object)
        self.test_archive()

    def test_archive(self):
        try:
            patoolib.test_archive(self.path)
            logger.debug(f'Testing file {self.path}')
            return True
        except patoolib.util.PatoolError as e:
            logger.error(
                f'Error. Testing {self.path} Failed with error {str(e)}')
            return False

    def check_integerity(self):
        if self.extension in patoolib.ArchiveFormats:
            self.test_archive()
        # not tested for documents & apks
        elif regex.search(
            r'.doc[x|m]?|.xls[x|m]?|.pp[t|s|x|m]+ \
                .od[b|c|f|g|m|p|t|s]+ .ap*2[k|x]+',
                self.extension,
                flags=regex.IGNORECASE) is not None:
            test_case = shutil.copyfile(self.path, f'{self.name}.zip')
            print(os.path.abspath(test_case))
            result = self.test_archive()
            os.remove(test_case)
            return result
        else:
            logger.debug('Integerity check not implemented for This file type! Skipping')
            return True


class OfficeDocumentFile(ArchiveFile):
    pass


class MediaFile(MyFile):
    pass
