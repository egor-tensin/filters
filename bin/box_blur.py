# Copyright 2016 (c) Egor Tensin <Egor.Tensin@gmail.com>
# This file is part of the "Simple image filters" project.
# For details, see https://github.com/egor-tensin/filters.
# Distributed under the MIT License.

import argparse
import sys

from .utils import cmd_line, image
from filters.convolution import convolve
from filters.kernel.box_blur import gen_kernel

DEFAULT_RADIUS = 1

def _main_box_blur(img_path, radius=DEFAULT_RADIUS, output_path=None):
    img = image.load_grayscale(img_path)
    kernel = gen_kernel(radius)
    output = convolve(img, kernel)
    if output_path is None:
        image.show(output)
    else:
        image.save(output_path, output)

def _parse_args(args=sys.argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('img_path')
    parser.add_argument('--output', '-o',
                        dest='output_path', default=None)
    parser.add_argument('--radius', '-r',
                        type=cmd_line.parse_non_negative_integer,
                        default=DEFAULT_RADIUS)
    return parser.parse_args(args[1:])

def _main(args=sys.argv):
    _main_box_blur(**vars(_parse_args(args)))

if __name__ == '__main__':
    _main()
