"""Logging mechanism test cases."""

import os
from sys import path, stderr, stdout

import pytest
from lib.Logger import Logger

from preferences import preferences

path.append("..")

test_logger = Logger("TestLogger")
TEST_PATH = "tests"
TEST_MSG = "Test message"
"""print('name',
      test_logger,
      '\n' * 4,
      test_logger.level)"""

test_logger.log(0, "This is unset level log")
test_logger.info("This is info level log")
test_logger.debug("This is debug level log")
test_logger.warning("This is warning level log")
test_logger.error("This is error level log")
test_logger.critical("This is critical level log")


def test_logger_init():
    """Test logger initialization."""
    assert isinstance(test_logger, Logger)


def test_logger_create_log_file():
    """Test logger log method."""
    test_logger.log(40, TEST_MSG)
    log_file = test_logger.log_file_name
    assert os.path.exists(log_file) and os.path.isfile(log_file)


def test_logger_log_to_file():
    """Test logger log method."""
    test_logger.log(5, TEST_MSG)
    assert test_logger["file"].readlines()[0] == TEST_MSG


def test_logger_log_to_std_out():
    """Test logger output to stdout or stderr."""
    test_logger.log(10, TEST_MSG)
    assert stdout.read() == TEST_MSG
    test_logger.log(10, TEST_MSG, stderr=True)
    assert stderr.read() == TEST_MSG


def test_logger_log_with_level():
    """Test logger log method with level."""
    test_logger.log(10, TEST_MSG, level="debug")
    assert test_logger.log_file.read() == TEST_MSG


def test_logger_log_with_level_and_file():
    """Test logger log method with level and file."""
    test_logger.log(10, TEST_MSGl="debug", file="test_logger.log")
    assert test_logger.log_file.read() == TEST_MSG


def test_logger_log_with_level_and_file_and_path():
    """Test logger log method with level, file and path."""
    test_logger.log(10,
                    TEST_MSG,
                    level="debug",
                    file="test_logger.log",
                    path=TEST_PATH)
    assert test_logger.log_file.read() == TEST_MSG


def test_logger_log_with_level_and_file_and_path_and_mode():
    """Test logger log method with level, file, path and mode."""
    test_logger.log(10,
                    TEST_MSG,
                    level="debug",
                    file="test_logger.log",
                    path=TEST_PATH,
                    mode="a")
    assert test_logger.log_file.read() == TEST_MSG


def test_logger_log_with_level_and_file_and_path_and_mode_and_encoding():
    """Test logger log method with level, file, path, mode and encoding."""
    test_logger.log(
        10,
        TEST_MSG,
        level="debug",
        file="test_logger_log_with_level_and_file_and_path_and_mode_and_encoding",
        path=TEST_PATH,
        mode="a",
        encoding="utf-8",
    )
    assert test_logger.log_file.read() == TEST_MSG
