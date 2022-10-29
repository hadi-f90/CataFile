from sys import path
import pytest
path.append('..')
path.append('.')

from lib import File

class Test_File_Magic_detect:
    
    @pytest.fixture()
    def file(self):
        return File.File()
    

    def test_magic_detect_1(self, file):
        file.magic_detect()


class Test_File_Fleep_detect:
    
    @pytest.fixture()
    def file(self):
        return File.File()
    

    def test_fleep_detect_1(self, file):
        result = file.fleep_detect()

