from simple_delete import rm
# our goal will be to mock the rm call to os.remove so that we don't actually
# touch the filesystem in calling rm.
# In our test, we mock 'simple_delete.os' because the thing that touches the filesystem
# is the call to os.remove() which is located *inside* our rm function.
# What we don't want to do is mock 'simple_delete.rm'

import os.path
import tempfile

from unittest import mock
import unittest

class RmTestCase(unittest.TestCase):

    tmpfilepath = os.path.join(tempfile.gettempdir(), "tmp-testfile")
    print(tmpfilepath)

    def setUp(self):
        print( "RmTestCase.setUp called")
        with open(self.tmpfilepath, "w") as f:
            f.write("Delete me!")

    @mock.patch('simple_delete.os.path') # we also want to mock out the call to isfile, which is in os.path
    @mock.patch('simple_delete.os') # because rm gets called *in* simple_delete.os
                                    # 'simple_delete.rm' is NOT what we want to do
    def test_rm(self, mock_os, mock_path): # mock_os is now our ENTIRE replaced mock'ed version
                                           # of the os module that is imported in simple_delete
        mock_path.isfile.return_value = False

        rm("any path")

        self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present")

        mock_path.isfile.return_value = True # this will make the file *exist* for us

        rm("any path")
        # now we run the check to see that rm was called correctly
        # note: we don't actually have to do this, since mocking out simple_delete.os
        # just won't do anything.
        # note: the mock_os object that gets passed into test_rm gives us access
        # to see just how rm was called inside the function
        # note: remove is a method of os and so we use mock_os.remove to access
        # some stuff about the mocked method
        mock_os.remove.assert_called_with("any path")
        self.assertEqual(mock_os.remove.call_count, 1)

    def test_rm_real(self):
        rm(self.tmpfilepath)
        # check to make sure that the file actually is removed since we
        # didn't mock rm this time
        self.assertFalse(os.path.isfile(self.tmpfilepath), "Failed to remove the file.")

if __name__ == '__main__':
    unittest.main()
