import os
import unittest


class TestFileSystem(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestFileSystem, self).__init__(*args, **kwargs)
        # self.gen_stubs()
        self.test_filename = 'test-file.txt'

    def _cleanup_test_file(self):
        if os.path.isfile(self.test_filename):
            os.remove(self.test_filename)

    def setUp(self):
        self._cleanup_test_file()

    def tearDown(self):
        self._cleanup_test_file()

    def test_read(self):
        test_string = 'hello world'
        with open(self.test_filename, 'w') as f:
            f.write(test_string)
        with open(self.test_filename) as f:
            res = f.read()
        self.assertEqual(res, test_string)

    def test_readline(self):
        with open(self.test_filename, 'w') as f:
            for i in range(5):
                f.write('%d\n' % i)
        i = 0
        with open(self.test_filename) as f:
            for line in f.readlines():
                self.assertEqual('%d\n' % i, line)
                i += 1


if __name__ == '__main__':
    unittest.main()
