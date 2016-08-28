# Copyright 2016 (c) Egor Tensin <Egor.Tensin@gmail.com>
# This file is part of the "Simple image filters" project.
# For details, see https://github.com/egor-tensin/filters.
# Distributed under the MIT License.

import argparse
from enum import Enum
import sys

import cv2
import numpy as np

class Direction(Enum):
    N = 'N'
    NE = 'NE'
    E = 'E'
    SE = 'SE'
    S = 'S'
    SW = 'SW'
    W = 'W'
    NW = 'NW'

    def gen_kernel(self, distance):
        radius = distance
        size = 2 * radius + 1
        kernel = np.zeros((size, size))
        x, y = radius, radius

        if self is Direction.N:
            x = -1
        elif self is Direction.NE:
            x, y = -1, 0
        elif self is Direction.E:
            y = 0
        elif self is Direction.SE:
            x, y = 0, 0
        elif self is Direction.S:
            x = 0
        elif self is Direction.SW:
            x, y = 0, -1
        elif self is Direction.W:
            y = -1
        elif self is Direction.NW:
            x, y = -1, -1
        else:
            raise NotImplementedError('unsupported direction: ' + str(self))

        kernel[x, y] = 1
        return kernel

    def __str__(self):
        return self.name

def convolve(img, kernel):
    #print(kernel)
    radius = kernel.shape[0] // 2
    output = np.zeros(img.shape, dtype=img.dtype)
    for i in range(radius, img.shape[0] - radius):
        for j in range(radius, img.shape[1] - radius):
            neighborhood = img[i - radius:i + radius + 1, j - radius:j + radius + 1]
            output[i, j] = np.sum(neighborhood * kernel)
    return output

DEFAULT_DIRECTION = Direction.SE
DEFAULT_DISTANCE = 1

def do(img_path, direction=DEFAULT_DIRECTION, distance=DEFAULT_DISTANCE,
       output_path=None):

    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    kernel = direction.gen_kernel(distance)
    output = convolve(img, kernel)
    if output_path is None:
        cv2.imshow("Output", output)
        cv2.waitKey()
    else:
        cv2.imwrite(output_path, output)

def _parse_direction(s):
    try:
        return Direction(s)
    except ValueError:
        raise argparse.ArgumentTypeError('invalid direction: ' + s)

def _parse_non_negative_integer(s):
    try:
        x = int(s)
    except ValueError:
        raise argparse.ArgumentTypeError('must be a non-negative integer: ' + s)
    if x < 0:
        raise argparse.ArgumentTypeError('must be a non-negative integer: ' + s)
    return x

def _parse_args(args=sys.argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('img_path')
    parser.add_argument('--output', '-o',
                        dest='output_path', default=None)
    parser.add_argument('--direction', '-d',
                        type=_parse_direction,
                        choices=Direction,
                        default=DEFAULT_DIRECTION)
    parser.add_argument('--distance', '-n',
                        type=_parse_non_negative_integer,
                        default=DEFAULT_DISTANCE)
    return parser.parse_args(args[1:])

def main(args=sys.argv):
    do(**vars(_parse_args(args)))

if __name__ == '__main__':
    main()
