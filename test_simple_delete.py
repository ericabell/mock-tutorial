from simple_delete import rm

import os.path
import tempfile

from unittest import mock
import unittest

class RmTestCase(unittest.TestCase):

    tmpfilepath = os.path.join(tempfile.gettempdir(), "tmp-testfile")
    print(tmpfilepath)

    def setUp(self):
        with open(self.tmpfilepath, "w") as f:
            f.write("Delete me!")

    @mock.patch('simple_delete.os')
    def test_rm(self, mock_os):
        rm("any path")
        mock_os.remove.assert_called_with("any path")

if __name__ == '__main__':
    unittest.main()
