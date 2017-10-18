#!/usr/bin/env python

# To upload a version to PyPI, run:
#
#    python setup.py sdist upload
#
# If the package is not registered with PyPI yet, do so with:
#
# python setup.py register

from distutils.core import setup
import os
import platform

VERSION = '3.2.0'

# Auto generate a __version__ package for the package to import
with open(os.path.join('spinapi', '__version__.py'), 'w') as f:
    f.write("__version__ = '%s'\n"%VERSION)

arch = platform.architecture()

if arch == ('32bit', 'ELF'):
    bundled_shared_objects = ['libspinapi.so']
elif arch == ('64bit', 'ELF'):
    bundled_shared_objects = ['libspinapi64.so']
else:
    bundled_shared_objects = []
    
setup(name='spinapi',
      version=VERSION,
      description='Python wrapper around the Spincore PulseBlaster API using ctypes.',
      author='Chris Billington',
      author_email='chrisjbillington@gmail.com',
      url='https://bitbucket.org/cbillington/spinapi/',
      license="BSD",
      packages=['spinapi'],
      package_data={'spinapi': bundled_shared_objects}
     )
