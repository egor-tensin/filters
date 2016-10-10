Simple image filters
====================

A collection of simple image processing utilities using basic convolution
matrices.

Prerequisites
-------------

* Python 3.4 or higher
* [numpy]
* [opencv-python]

The versions below have been verified to work properly.

Software      | Version
------------- | -------
CPython       | 3.5.1
numpy         | 1.11.0
opencv-python | 3.1.0

[numpy]: http://www.numpy.org/
[opencv-python]: http://opencv.org/

Windows binaries for CPython can be acquired at
http://www.lfd.uci.edu/~gohlke/pythonlibs/.

OpenCV's Python bindings require [Visual C++ Redistributable for Visual Studio
2015] on Windows.

[Visual C++ Redistributable for Visual Studio 2015]: https://www.microsoft.com/en-us/download/details.aspx?id=48145

Usage
-----

Run the scripts from the top-level directory using `python -m`.
Pass the `--help` flag to a script to examine its detailed usage information.

For example (using Windows-style paths):

    > python -m bin.box_blur img\Lenna.png --radius 3

The complete list of usable scripts is given below.

* box_blur.py &mdash; Apply box blur to an image.
* gaussian_blur.py &mdash; Apply Gaussian blur to an image.
* shift.py &mdash; Shift an image by a few pixels in a specified direction.

Development
-----------

### Linting

Requires [PyLint].
To lint everything, run from the top-level directory:

    > pylint filters
    ...

    > pylint bin
    ...

[PyLint]: https://www.pylint.org/

License
-------

Distributed under the MIT License.
See [LICENSE.txt] for details.

[LICENSE.txt]: LICENSE.txt
