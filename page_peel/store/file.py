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

print __name__
print __module__
class FileStore(object):
    """
    ``FileStore`` is a store class that deals with files from a directory.

    A store is an object which can retrieve content from a document, and save
    new content to a document. A store document is usually an HTML document.
    Where it is saved and how it is retrieved is defined by the store
    implementation. We can have, for example, stores to manage documents from
    the local filesystem, or manage documents via FTP or SSH etc. Each
    document has an "address", which usually is an HTTP URL. It is up to the
    store to map the URL to an editable document, if it is supposed to be
    altered.

    ``FileStore`` knows two things: a URL that points to a document, and a
    directory where an identical document can be found::

    >>> import tempfile
    >>> tempdir = tempfile.mkdtemp()
    >>> store = FileStore(
    ...     base_address='http://test.com', directory=tempdir)

    When we call ``FileStore.read()`` giving it a URL, it will remove the base
    address from the given URL, and then try to find a file with whatever
    remains::

    >>> from inelegant.fs import temp_file
    >>> with temp_file(dir=tempdir, name='index.html', content='Hello'):
    ...     store.read('http://test.com/index.html')
    'Hello'

    We can also change it with ``write()``::

    >>> with temp_file(dir=tempdir, name='index.html', content='Hello'):
    ...     store.read('http://test.com/index.html')
    ...     store.write('http://test.com/index.html', 'CHANGED')
    ...     store.read('http://test.com/index.html')
    'Hello'
    'CHANGED'
    """

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
