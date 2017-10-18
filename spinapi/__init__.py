try:
    from .__version__ import __version__
except ImportError:
    # Version file has not been autogenerated from build process:
    __version__ = None

from .spinapi import *
