# spinapi

Python wrapper around the Spincore PulseBlaster API using ctypes.
( 
[view on pypi](https://pypi.python.org/pypi/spinapi/);
[view on Bitbucket](https://bitbucket.org/cbillington/spinapi)
)

   * Install `python setup.py install`.
   * This package assumes that the spincore API is installed on your system.
   * You should install whichever spincore API has the same bit count - 32 or 64 - for your operating system, not your python installation. If you use 32 bit Python but 64 bit windows, you should still install the 64 bit spincore API. It provides 32 bit dlls as well, which this wrapper will use in that case. Installing the 64 bit spincore API ensures you have the correct USB device drivers Windows will require to talk to the PulseBlaster.
