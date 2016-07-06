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


from setuptools import setup, find_packages

setup(
    name="Page Peel",
    version="0.0.1.dev1",
    author='Adam Victor Brandizzi',
    author_email='adam@brandizzi.com.br',
    description='Page Peel - editable web pages',
    license='LGPLv3',
    url='http://bitbucket.com/brandizzi/page-peel',

    packages=find_packages(),
    test_suite='page_peel_tests',
    test_loader='unittest:TestLoader',
    tests_require=['inelegant']
)
