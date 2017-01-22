# Copyright 2016 (c) Egor Tensin <Egor.Tensin@gmail.com>
# This file is part of the "Simple image filters" project.
# For details, see https://github.com/egor-tensin/filters.
# Distributed under the MIT License.

import argparse
import sys

from filters.convolution import convolve
from filters.kernel.box_blur import gen_kernel

from .utils import cmd_line, image

DEFAULT_RADIUS = 1

def do_box_blur(img_path, radius=DEFAULT_RADIUS, output_path=None):
    img = image.load_grayscale(img_path)
    kernel = gen_kernel(radius)
    output = convolve(img, kernel)
    if output_path is None:
        image.show(output)
    else:
        image.save(output_path, output)

def _parse_args(args=None):
    if args is None:
        args = sys.argv[1:]
    parser = argparse.ArgumentParser(
        description='Apply box blur to an image.')
    parser.add_argument('img_path', help='source image file path')
    parser.add_argument('--output', '-o', dest='output_path', default=None,
                        help='save new image to a file')
    parser.add_argument('--radius', '-r',
                        type=cmd_line.parse_non_negative_integer,
                        default=DEFAULT_RADIUS,
                        help='specify convolution kernel radius')
    return parser.parse_args(args)

def main(args=None):
    do_box_blur(**vars(_parse_args(args)))

if __name__ == '__main__':
    main()
