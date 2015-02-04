#!/usr/bin/env python

try:
    from setuptools import setup,find_packages
except ImportError:
    from distutils.core import setup

config = {
    'name': 'bloxmain',
    'description': 'blox-main',
    'author': 'Michael Pollett',
    'author_email': 'mike@pollett.co.uk',
    'version': '0.1',
    'install_requires': ['nose','paramiko>1.10','configobj'],
    'namespace_packages': ['blox','blox.modules'],
    'packages': find_packages(),
    'scripts': [ 'bin/blox' ],
    'data_files': [ ('/etc', ['config/blox.conf'] ), ('/etc/init.d', ['init/blox'] ) ]
}

setup(**config)
