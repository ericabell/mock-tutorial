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

    @mock.patch('simple_delete.os') # because rm gets called *in* simple_delete.os
    def test_rm(self, mock_os):
        rm("any path")
        # now we run the check to see that rm was called correctly
        # note: we don't actually have to do this, since mocking out simple_delete.os
        # just won't do anything.
        mock_os.remove.assert_called_with("any path")

    def test_rm_real(self):
        rm(self.tmpfilepath)
        self.assertFalse(os.path.isfile(self.tmpfilepath), "Failed to remove the file.")

if __name__ == '__main__':
    unittest.main()
