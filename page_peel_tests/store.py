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

import unittest

import textwrap

from page_peel.store import FakeStore


class TestStore(unittest.TestCase):
    """
    "Stores" are objects that effectively retrieve the content of documents to
    be edited, as well as save new content to the document if possible. This
    test specifies the interface for stores.
    """

    def get_store(self, uri, content):
        """
        Returns an instance of the store. By default, the returned
        implementation is a fake cake.
        """

        doc = "My message"

        return FakeStore(documents={uri: content})

    def test_read(self):
        """
        A store should read the content of a document and return it.
        """

        store = self.get_store(
            uri='http://localhost:9000/index.html', content="My message")
        content = store.read('http://localhost:9000/index.html')

        self.assertEquals(content, "My message")

    def test_write(self):
        """
        A store should write content into a document... eventually. If the
        page editor has means and permissions, of course.
        """

        store = self.get_store(
            uri='http://localhost:9000/index.html', content="My message")
        store.write('http://localhost:9000/index.html', "New message")

        content = store.read('http://localhost:9000/index.html')

        self.assertEquals(content, "New message")
