#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path

class RemovalService(object):
    """
    A service for removing objects from the filesystem
    """
    def rm(self, filename):
        if os.path.isfile(filename):
            os.remove(filename)
