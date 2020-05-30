from setuptools import setup
import os
import platform

VERSION = '3.2.2'

# Auto generate a __version__ package for the package to import
with open(os.path.join('spinapi', '__version__.py'), 'w') as f:
    f.write("__version__ = '%s'\n"%VERSION)

arch = platform.architecture()

bundled_shared_objects = ['libspinapi.so', 'libspinapi64.so']
    
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
