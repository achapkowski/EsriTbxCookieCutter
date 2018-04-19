#!/usr/bin/env {{cookiecutter.python}}
# vim: set fileencoding=utf-8
# pylint:disable=line-too-long
r""":mod:`test{{cookiecutter.project_name}}` - unittests for {{cookiecutter.project_name}}
##########################################

.. module:: test{{cookiecutter.project_name}}
   :synopsis: {{cookiecutter.short_description}}
.. moduleauthor:: {{cookiecutter.author}} <{{cookiecutter.email}}>

Comprehensive unittests for {{cookiecutter.project_name}}

..
   {{cookiecutter.copyright}}"""
# pylint:enable=line-too-long
# ----------------------------------------------------------------------------
# Standard library imports
# ----------------------------------------------------------------------------
import logging
import unittest

# ----------------------------------------------------------------------------
# Module level initializations
# ----------------------------------------------------------------------------
__version__    = '{{cookiecutter.release}}'
__author__     = '{{cookiecutter.author}}'
__email__      = '{{cookiecutter.email}}'
__status__     = 'Testing'
__copyright__  = '{{cookiecutter.copyright}}'
__year__ = '{{cookiecutter.year}}'

LOG = logging.getLogger('test{{cookiecutter.project_name}}')

import {{cookiecutter.file_name}}


class Test{{cookiecutter.project_name}}(unittest.TestCase):
    r"""{{cookiecutter.project_name}} unittest test case"""

    # pylint: disable=invalid-name

    def setUp(self):
        r"""initialize test fixture"""
        pass

    def tearDown(self):
        r"""tear down test fixture"""
        pass


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())