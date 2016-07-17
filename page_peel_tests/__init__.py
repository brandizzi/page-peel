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

from inelegant.finder import TestFinder

load_tests = TestFinder(
    'page_peel.store',
    'page_peel.store.fake',
    'page_peel.store.file',
    'page_peel_tests.store'
).load_tests
