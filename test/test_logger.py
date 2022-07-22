import os
import sys
import unittest

sys.path.append('.')

import project.logger as logger
from jalali.Jalalian import jdate


class Testlogger(unittest.TestCase):
    msgs = ['This is a warning',
            'This is a debug',
            'This is an info',
            'This is an error',
            'This is a critical']

    def test_creating_log_file(self):
        return self.assertTrue(os.path.exists(logger.LOG_FILE))

    def test_writing_msg(self):
        logger.log.warning('This is a warning')
        logger.log.debug('This is a debug')
        logger.log.info('This is an info')
        logger.log.error('This is an error')
        logger.log.critical('This is a critical')

        with open(logger.LOG_FILE, 'r') as f:
            saved_msgs = f.readlines()

            for _ in msgs:
                for m in saved_msgs:
                    self.assertIn(_, m)


if __name__ == '__main__':
    unittest.main()
