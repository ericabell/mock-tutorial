from simple_delete import rm

from unittest.mock import MagicMock as mock
import unittest

class RmTestCase(unittest.TestCase):

    @mock.patch('mymodule.os')
    def test_rm(self, mock_os):
        rm("any path")
        mock_os.remove.assert_called_with("any path")

if __name__ == '__main__':
    unittest.main()
