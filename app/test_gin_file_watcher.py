import unittest
import gin_file_watcher
import constants
import os
import unittest.mock as mock
import time

class TestGinFileWatcher(unittest.TestCase):

    def test_gin_file_watcher(self):
        ##  should match and trigger for files in the folder
        with mock.patch('gin_file_watcher.on_created') as on_created:
            file_thread = gin_file_watcher.get_watchdog_thread()
            file_thread.start()
            os.system('> {}/test.gin'.format(constants.SAVE_DIR))
            time.sleep(4)
            self.assertTrue(on_created.called)
        ##  should not match and not trigger for files not in the folder
        with mock.patch('gin_file_watcher.on_created') as on_created:
            file_thread = gin_file_watcher.get_watchdog_thread()
            file_thread.start()
            os.system('> {}/test.gin'.format('assets'))
            time.sleep(4)
            self.assertFalse(on_created.called)


if __name__ == '__main__':
    unittest.main()