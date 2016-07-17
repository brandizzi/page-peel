#!/usr/bin/env python
# coding: utf-8
#
# Copyright 2016 Adam Victor Brandizzi
#
# This file is part of Page Peel.
#
# Page Peel is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# Page Peel is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for
# more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Inelegant.  If not, see <http://www.gnu.org/licenses/>.

import os.path


class FileStore(object):

    def __init__(self, base_address, directory):
        self.base_address = base_address
        self.directory = directory

    def read(self, address):
        path = os.path.join(
            self.directory, address.replace(self.base_address, '')[1:])

        with open(path) as f:
            return f.read()

    def write(self, address, content):
        path = os.path.join(
            self.directory, address.replace(self.base_address, '')[1:])

        with open(path, 'w') as f:
            return f.write(content)
