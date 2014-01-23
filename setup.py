#!/usr/bin/env python

# To upload a version to PyPI, run:
#
#    python setup.py sdist upload
#
# If the package is not registered with PyPI yet, do so with:
#
# python setup.py register

from distutils.core import setup

setup(name='spinapi',
      version='1.0.2',
      description='Python wrapper around the Spincore PulseBlaster API using ctypes.',
      author='Chris Billington',
      author_email='chrisjbillington@gmail.com',
      url='https://bitbucket.org/cbillington/spinapi/',
      license="BSD",
      packages=['spinapi']
     )
