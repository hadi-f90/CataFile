"""Logging mechanism test cases."""

from sys import path, stderr, stdout

path.append("..")
import pytest
from lib.KonsoleLogger import *
from logging import Logger
# from preferences import preferences

test_logger = konsole
TEST_PATH = 'tests'
TEST_MSG = 'Test message'

"""print('name',
      test_logger,
      '\n' * 4,
      test_logger.level)"""



test_logger.log(0, f'{DATE_TIME} This is unset level log {DATE_TIME}')
test_logger._main_logger.level = logging.NOTSET
# test_logger.trace('This is trace level log')
test_logger.info(f'{DATE_TIME} This is info level log')
test_logger.debug('This is debug level log')
test_logger.warning('This is warning level log')
test_logger.error('This is error level log')
# test_logger.success("This is success level log")
test_logger.critical(f'This is critical level log {DATE_TIME}')


def test_logger_init():
    """Test logger initialization."""
    assert isinstance(test_logger, Logger)


def test_logger_log_to_file():
    """Test logger log method."""
    test_logger.log(5, TEST_MSG)
    assert test_logger['file'].readlines()[0] == TEST_MSG


def test_logger_log_to_std_out():
    """Test logger output to stdout or stderr."""
    test_logger.log(10, TEST_MSG)
    assert stdout.read() == TEST_MSG
    test_logger.log(10, TEST_MSG, stderr=True)
    assert stderr.read() == TEST_MSG


def test_logger_log_with_level():
    """Test logger log method with level."""
    test_logger.log(10, TEST_MSG, level='debug')
    assert test_logger.log_file.read() == TEST_MSG


def test_logger_log_with_level_and_file():
    """Test logger log method with level and file."""
    test_logger.log(10, TEST_MSGl='debug', file='test_logger.log')
    assert test_logger.log_file.read() == TEST_MSG


def test_logger_log_with_level_and_file_and_path():
    """Test logger log method with level, file and path."""
    test_logger.log(10, TEST_MSG, level='debug', file='test_logger.log',
                    path=TEST_PATH)
    assert test_logger.log_file.read() == TEST_MSG


def test_logger_log_with_level_and_file_and_path_and_mode():
    """Test logger log method with level, file, path and mode."""
    test_logger.log(10, TEST_MSG, level='debug', file='test_logger.log',
                    path=TEST_PATH, mode='a')
    assert test_logger.log_file.read() == TEST_MSG


def test_logger_log_with_level_and_file_and_path_and_mode_and_encoding():
    """Test logger log method with level, file, path, mode and encoding."""
    test_logger.log(10, TEST_MSG, level='debug', file='test_logger_log_with_level_and_file_and_path_and_mode_and_encoding',
                    path=TEST_PATH, mode='a', encoding='utf-8')
    assert test_logger.log_file.read() == TEST_MSG
