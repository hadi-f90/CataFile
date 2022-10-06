import os
import shutil

import fleep
import magic
import patoolib
import regex
from fontbro import Font

from lib.Logger import LOGGER
from preferences import preferences


def create_proper_file_instance():
    """Summary: Creat List of files.

    Try to detect file type and creates an instance of it
    based on its mime type.

    Gets:
        A file_object

    Returns: List of files.
    """


# ============================== file object class ============================
class MyFile():
    """A class to manipulate  files."""

    def __init__(self, file_object=None):
        """Get a file object and create a MyFile instance.

        Args:
            file_object ( file type ): Defaults to None.
        """
        # file type info
        self.file_object = open(file_object, 'rb')
        self.path = os.path.abspath(file_object)
        self.file_name, self.extension = os.path.splitext(self.path)
        self.file_header = self.file_object.read(2048)
        if preferences.get('file_processor') == 0:
            self.fleep_detect()

        elif preferences.get('file_processor') == 1:
            self.mime = self.extension = self.magic_detect()

        elif preferences.get('file_processor') == 2:
            self.mime = self.extension

        else:
            LOGGER.error('file_processor not set')
        # self.extension_revert()

    def magic_detect(self):
        """Detect file type using magic module."""
        self.mime = magic.from_buffer(self.file_header, mime=True)
        self.type, self.detected_extension = self.mime.split('/')
        if self.mime == ('', None):
            self.mime = 'etc'

    def fleep_detect(self):
        """Detect file type using fleep module."""
        self.file_info = fleep.get(self.file_header)
        self.type = self.file_info.type[0]
        self.detected_extension = self.file_info.extension[0]
        self.mime = self.file_info.mime
        self.mime = 'etc' if len(self.mime) < 1 else self.file_info.mime[0]

    def file_date_time(self):
        """
        Return a tuple containing file datetime information.

        output: (accessed, created, modified)
        """
        # To-do: returns file data and time
        return (os.path.getatime(self.path),
                os.path.getctime(self.path),
                os.path.getmtime(self.path))

    def move(self, destination):
        """Move file to  given destination.

        Args:
            destination : str or path-like object
        """
        try:
            shutil.move(self.path, destination)
            LOGGER.info('Moved %s to %s.', self.path, destination)
            self.path = destination + self.file_name + self.extension

        except Exception as e:
            LOGGER.error('Error moving %s to %s.', self.path, destination)
            LOGGER.error(e)

    def copy(self, destination):
        """Copy file to given destination.

        Args:
            destination : str or path-like object
        """
        shutil.copy(self.path, destination)
        LOGGER.info('%s copied to %s', self.path, destination)

    def rename(self, new_name):
        """
        Change the name of the file to a new given name.

        new_name: str
        """
        LOGGER.info('Changing %s name to %s', self.path, new_name )
        try:
            os.rename(self.path, new_name)

        except FileExistsError as e:
            LOGGER.error('%s already exists. Numbering ...', new_name)
            LOGGER.error(e)

            number = 0
            new_file_name = f'{self.file_name}({number}).{self.extension}'
            while os.path.exists(new_file_name):
                number += 1
                new_file_name = f'{self.file_name}({number}).{self.extension}'
            os.rename(self.path, new_file_name)
            LOGGER.info('%s renamed to %s', self.path, new_file_name )

    def extension_revert(self):
        """Revert the extension of the file to the original one."""
        # if the file type is not known then try fo file its type
        if self.extension in (None, '') or self.detected_extension != self.extension:
            LOGGER.info('Changing %s extension to %s', self.path, self.detected_extension)
            new_name = f'{self.file_name}.{self.detected_extension}'
            self.rename(new_name)
            self.extension = self.detected_extension
            self.path = os.path.abspath(new_name)

    def __str__(self) -> str:
        """Return string representation name of the class instance."""
        return self.path


class FontFile(MyFile, Font):
    """Special class for font file actions that inherits MyFile & Font methods."""
    def __init__(self, file_object=None):
        """Initialize the font file actions."""
        super().__init__(file_object)
        self.font = Font(file_object)
        self.extension = self.font.get_format()
        self.font_name = self.font.get_name(key=Font.NAME_FAMILY_NAME)
        self.version = self.font.get_version()
        self.weight = self.font.get_weight()['name']

        # self.revert_font_name()

    def revert_font_name(self):  # not testes Yet!
        """Revert font file name to its internal name."""
        new_font_name = f'{self.font_name}-{self.weight}.{self.extension}'
        self.rename(new_font_name)
        LOGGER.info('Font reverted to its name: %s', self.file_name)
        self.file_name = new_font_name


class ArchiveFile(MyFile):
    """Archive File Type special class."""

    def __init__(self, file_object=None):
        super().__init__(file_object)
        # self.test_archive()

    def test_archive(self):
        """Test archive file health."""
        try:
            patoolib.test_archive(self.path)
            LOGGER.debug('Testing file %s', self.path)
            return True
        except patoolib.util.PatoolError as e:
            LOGGER.error(
                'Error. Testing %s Failed with error %s', self.path, e)
            return False

    def check_integerity(self):
        """Check an undetectable file."""
        if self.extension in patoolib.ArchiveFormats:
            self.test_archive()
        # not tested for documents & apks
        elif regex.search(
            r'.doc[x|m]?|.xls[x|m]?|.pp[t|s|x|m]+| \
                .od[b|c|f|g|m|p|t|s]+|.ap*2[k|x]+',
                self.extension,
                flags=regex.IGNORECASE) is not None:
            test_case = shutil.copyfile(self.path, f'{self.file_name}.zip')
            print(os.path.abspath(test_case))
            result = self.test_archive()
            os.remove(test_case)
            return result

        else:
            LOGGER.debug("Checking %s not supported!", self.extension)
            return False


class OfficeDocumentFile(ArchiveFile):
    """Will Process Documents."""


class MediaFile(MyFile):
    """Will process Media files e.g mp4, wav, etc."""
