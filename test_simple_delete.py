#!/usr/bin/env python

from simple_delete import rm

import os.path
import tempfile
import unittest

class RmTestCase(unittest.TestCase):
    tmpfilepath = os.path.join(tempfile.gettempdir(), "tmp-testfile")

    def setUp(self):
        with open(self.tempfilepath, "wb") as f:
            f.write("Delete me!")

    def test_rm(self):
        rm(self.tmpfilepath)
        self.assertFalse(os.path.isfile(self.tmpfilepath, "Failed to remove the file.")
