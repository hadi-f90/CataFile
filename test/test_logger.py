import os
import sys

from jalali.Jalalian import jdate

import project.logger as Logger

sys.path.append(".")

test_logger = Logger.Logger()

print(
    "name",
    test_logger.name,
    "\n" * 4,
    "formatter",
    test_logger.formatter,
    "\n" * 4,
    test_logger.level,
    test_logger.log,
    test_logger.log_file,
)
""" class Testlogger(unittest.TestCase):
    msgs = ['This is a warning',
            'This is a debug',
            'This is an info',
            'This is an error',
            'This is a critical']

    def test_logger(self):
        logger = Logger()
        for msg in self.msgs:
            logger.log(msg)
            self.assertIn(logger.log_file.readline(), msg)

    def test_creating_log_file(self):
        logger = Logger()
        return self.assertTrue(os.path.exists(logger.log_file))

    def test_writing_msg(self):
        logger = Logger()
        logger.log.warning('This is a warning')
        logger.log.debug('This is a debug')
        logger.log.info('This is an info')
        logger.log.error('This is an error')
        logger.log.critical('This is a critical')

        with open(logger.LOG_FILE, 'r') as f:
            saved_msgs = f.readlines()
            global msgs
            for _ in msgs:
                for m in saved_msgs:
                    self.assertIn(_, m)


if __name__ == '__main__':
    unittest.main() """
