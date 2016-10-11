# Copyright 2016 (c) Egor Tensin <Egor.Tensin@gmail.com>
# This file is part of the "Simple image filters" project.
# For details, see https://github.com/egor-tensin/filters.
# Distributed under the MIT License.

import argparse
import sys

from .utils import cmd_line, image
from filters.convolution import convolve
from filters.kernel.shift import Direction

DEFAULT_DIRECTION = Direction.SOUTH_EAST
DEFAULT_DISTANCE = 1

def _main_shift(
        img_path, direction=DEFAULT_DIRECTION, distance=DEFAULT_DISTANCE,
        output_path=None):

    img = image.load_grayscale(img_path)
    kernel = direction.gen_kernel(distance)
    output = convolve(img, kernel)
    if output_path is None:
        image.show(output)
    else:
        image.save(output_path, output)

def _parse_direction(s):
    try:
        return Direction(s)
    except ValueError:
        raise argparse.ArgumentTypeError('invalid direction: ' + s)

def _parse_args(args=sys.argv):
    parser = argparse.ArgumentParser(
        description='Shift an image by a few pixels in a specified direction.')
    parser.add_argument('img_path', help='source image file path')
    parser.add_argument('--output', '-o', dest='output_path', default=None,
                        help='save new image to a file')
    parser.add_argument('--direction', '-d', choices=Direction,
                        type=_parse_direction, default=DEFAULT_DIRECTION,
                        help='specify shifting direction')
    parser.add_argument('--distance', '-n',
                        type=cmd_line.parse_non_negative_integer,
                        default=DEFAULT_DISTANCE,
                        help='specify shift size (in pixels)')
    return parser.parse_args(args[1:])

def _main(args=sys.argv):
    _main_shift(**vars(_parse_args(args)))

if __name__ == '__main__':
    _main()
