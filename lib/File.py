"""This file contains a set of classes used to manipulate different file types."""
import os
import pathlib
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


class File:
    """A class to manipulate  files."""

    def __init__(self, file_object):
        """Get a file object and create a MyFile instance.

        Args:
            file_object ( file type ): Defaults to None.
        """
        # Todo: use pathlib for later versions
        # file type info
        self.full_path = pathlib.Path(file_object).resolve()
        self.parent_dir = self.full_path.parent
        self.full_file_name = self.full_path.name
        self.extension = self.full_path.suffix
        self.file_name = self.full_path.stem

        self.file_object = open(file_object, "rb")
        self.file_header = self.file_object.read(1024)

        if preferences.get("file_processor") == 0:
            self.fleep_detect()

        elif preferences.get("file_processor") == 1:
            self.magic_detect()

        elif preferences.get("file_processor") == 2:
            self.mime = self.extension

        else:
            LOGGER.error("File_processor not set")
            # self.extension_revert()
        LOGGER.debug(
            """Class file data:
                fullpath:%s
                parent_dir: %s
                full file name: %s
                extension: %s
                file name: %s
                file header:\n%s
                mime: %s""",
            self.full_path,
            self.parent_dir,
            self.full_file_name,
            self.extension,
            self.file_name,
            self.file_header,
            self.mime,
        )

    def magic_detect(self):
        """Detect file type using magic module."""
        self.mime = magic.from_buffer(self.file_header, mime=True)
        self.type, self.detected_extension = self.mime.split("/")
        self.detected_extension = f".{self.detected_extension}"
        if self.mime == ("", None):
            self.mime = "etc"

    def fleep_detect(self):
        """Detect file type using fleep module."""
        self.file_info = fleep.get(self.file_header)
        self.type = self.file_info.type[0]
        self.detected_extension = f".{self.file_info.extension[0]}"
        self.mime = self.file_info.mime
        self.mime = "etc" if len(self.mime) < 1 else self.file_info.mime[0]

    def file_date_time(self):
        """
        Return a tuple containing file datetime information.

        output: (accessed, created, modified)
        """
        # To-do: returns file data and time
        return (
            os.path.getatime(self.full_path),
            os.path.getctime(self.full_path),
            os.path.getmtime(self.full_path),
        )

    def move(self, destination):
        """Move file to  given destination.

        Args:
            destination : str or path-like object
        """
        LOGGER.debug(
            "variable data:\nself path: %s\ndestination: %s\n",
            self.full_path,
            destination,
        )
        destination = self._path_check(destination)
        try:
            shutil.move(self.full_path, destination)
            self.full_path = destination
            LOGGER.info("Moved %s to %s.", self.full_path, destination)

        except Exception as error:
            LOGGER.error(
                "Error moving %s to %s because of:\n%s.",
                self.full_path,
                destination,
                error,
            )
            LOGGER.exception("Deatiled exception: %s", error)

    def copy(self, destination):
        """Copy file to given destination.

        Args:
            destination : str or path-like object
        """
        destination = self._path_check(destination)
        LOGGER.debug(
            "variable data:\nself path: %s\ndestination: %s\n",
            self.full_path,
            destination,
        )
        shutil.copy(self.full_path, destination)
        LOGGER.info("%s copied to %s", self.full_path, destination)

    def _path_check(self, path):
        if not pathlib.Path(path).exists():
            os.mkdir(path)
        LOGGER.debug("Destination changed from %s to %s", path, path)
        return path

    def rename(self, new_name):
        """
        Change the name of the file to a new given name.

        new_name: str
        """
        LOGGER.info("Changing %s name to %s", self.full_path, new_name)
        try:
            pathlib.Path(self.full_path).rename(new_name)

        except FileExistsError as error:
            LOGGER.debug(error)
            LOGGER.info("%s already exists. Numbering ...", new_name)

            number = 0
            new_file_name = f"{self.file_name}({number}).{self.extension}"
            while pathlib.Path(new_file_name).exists():
                number += 1
                new_file_name = f"{self.file_name}({number}).{self.extension}"
            pathlib.Path(self.full_path).rename(new_file_name)
            LOGGER.info("%s renamed to %s", self.full_path, new_file_name)

    def extension_revert(self):
        """Revert the extension of the file to the original one."""
        # if the file type is not known then try fo file its type
        if self.extension in (None,
                              "") or self.detected_extension != self.extension:
            LOGGER.info("Changing %s extension to %s", self.full_path,
                        self.detected_extension)
            new_name = self.full_path.with_suffix(self.detected_extension)
            self.rename(new_name)
            self.extension = self.detected_extension
            self.full_path = pathlib.PurePath(new_name)

    def __str__(self) -> str:
        """Return string representation name of the class instance."""
        return self.full_path


class FontFile(File, Font):
    """Special class for font file actions that inherits MyFile & Font methods."""

    def __init__(self, file_object=None):
        """Initialize the font file actions."""
        super().__init__(file_object)
        self.font = Font(file_object)
        self.extension = self.font.get_format()
        self.font_name = self.font.get_name(key=Font.NAME_FAMILY_NAME)
        self.version = self.font.get_version()
        self.weight = self.font.get_weight()["name"]

        # self.revert_font_name()

    def revert_font_name(self):  # not testes Yet!
        """Revert font file name to its internal name."""
        new_font_name = f"{self.font_name}-{self.weight}.{self.extension}"
        self.rename(new_font_name)
        LOGGER.info("Font reverted to its name: %s", self.file_name)
        self.file_name = new_font_name


class ArchiveFile(File):
    """Archive File Type special class."""

    def __init__(self, file_object=None):
        """Initialize a ArchiveFile object based File"""
        super().__init__(file_object)
        # self.test_archive()

    def test_archive(self):
        """Test archive file health."""
        try:
            patoolib.test_archive(self.full_path)
            LOGGER.debug("Testing file %s", self.full_path)
            return True
        except patoolib.util.PatoolError as error:
            LOGGER.error("Error. Testing %s Failed with error %s",
                         self.full_path, error)
            return False

    def check_integerity(self):
        """Check an undetectable file."""
        if self.extension in patoolib.ArchiveFormats:
            return self.test_archive()
        # not tested for documents & apks
        if (regex.search(
                r".doc[x|m]?|.xls[x|m]?|.pp[t|s|x|m]+| \
                .od[b|c|f|g|m|p|t|s]+|.ap*2[k|x]+",
                self.extension,
                flags=regex.IGNORECASE,
        ) is not None):
            test_case = shutil.copyfile(self.full_path,
                                        f"{self.file_name}.zip")
            print(os.full_path.abspath(test_case))
            result = self.test_archive()
            os.remove(test_case)
            return result

        LOGGER.debug("Checking %s not supported!", self.extension)
        return False


class OfficeDocumentFile(ArchiveFile):
    """Will Process Documents."""


class MediaFile(File):
    """Will process Media files e.g mp4, wav, etc."""
