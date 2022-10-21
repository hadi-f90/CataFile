import pytest

from lib import File


class Test_File_Magic_detect:

    @pytest.fixture()
    def file(self):
        return File.File()

    def test_magic_detect_1(self, file):
        result = file.magic_detect()
