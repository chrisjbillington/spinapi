# spinapi

Python wrapper around the SpinCore PulseBlaster API using ctypes.

(
[view on PyPI](https://pypi.org/project/spinapi/);
[view on GitHub](https://github.com/chrisjbillington/spinapi)
)

## Installation

```
pip install spinapi
```

or

```
conda install -c labscript-suite spinapi
```

spinapi supports Windows and Linux on x86 and x86-64.

On Windows, spinapi loads `spinapi64.dll` (64-bit Python) or `spinapi.dll` (32-bit
Python) from the system directories. Install
[SpinAPI from SpinCore](https://www.spincore.com/support/spinapi/), which puts the
library there and installs the USB drivers for the PulseBlaster. Install the SpinAPI
build with the same bit count as Windows, not as Python: the 64-bit SpinAPI also
provides the 32-bit library.

On Linux, the SpinCore library is bundled with spinapi. It requires libusb-0.1, which
most distributions provide in a package named `libusb-compat` or `libusb-0.1-4`.
