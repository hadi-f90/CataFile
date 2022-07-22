import unittest
import os
import project.logger as logger


class Testlogger(unittest.TestCase):
    def creating_log_file(self):
        self.assertTrue(os.path.exists(logger.LOG_FILE))

    def writing_msg(self):
        logger.log.warning('This is a warning')
        logger.log.debug('This is a debug')
        logger.log.info('This is an info')
        logger.log.error('This is an error')
        logger.log.critical('This is a critical')

        f = open(logger.LOG_FILE, 'r')
        saved_msgs = f.readlines()
        msgs = ['This is a warning',
                'This is a debug',
                'This is an info',
                'This is an error',
                'This is a critical']

        for _ in msgs:
            self.assertIn(_, saved_msgs)


if __name__ == '__main__':
    unittest.main()