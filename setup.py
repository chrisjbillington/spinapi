#!/usr/bin/env python

from distutils.core import setup

setup(name='spinapi',
      version='1.0',
      description='Python wrapper around the Spincore PulseBlaster API using ctypes.',
      author='Chris Billington',
      author_email='chrisjbillington@gmail.com',
      url='https://bitbucket.org/cbillington/spinapi/',
      license="BSD",
      packages=['spinapi'],
      package_data={'spinapi': ['LICENSE.txt', 'README.md']}
     )
