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


class FakeStore(object):
    """
    ``FakeStore`` is a "fake cake" implementation of stores.

    A store is an object which can retrieve content from a document, and save
    new content to a document. A store document is usually an HTML document.
    Where it is saved and how it is retrieved is defined by the store
    implementation. We can have, for example, stores to manage documents from
    the local filesystem, or manage documents via FTP or SSH etc. Each
    document has an "address", which usually is an HTTP URL. It is up to the
    store to map the URL to an editable document, if it is supposed to be
    altered.

    As a fake cake, ``FakeStore`` defines the common functional behaviors
    expected from all stores. Its constructor expects a dict mapping URLs to
    contents::

    >>> store = FakeStore({
    ...     'http://test.com/index.html': '<html><body>ok</body></html>'
    ... })

    We can retrieve the content of a store with ``read()``::

    >>> store.read('http://test.com/index.html')
    '<html><body>ok</body></html>'

    We can also change it with ``write()``::

    >>> store.write(
    ...     'http://test.com/index.html', '<html><body>CHANGED</body></html>')
    >>> store.read('http://test.com/index.html')
    '<html><body>CHANGED</body></html>'
    """

    def __init__(self, documents):
        self.documents = documents

    def read(self, address):
        return self.documents[address]

    def write(self, address, content):
        self.documents[address] = content
