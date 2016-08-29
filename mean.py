# Copyright 2016 (c) Egor Tensin <Egor.Tensin@gmail.com>
# This file is part of the "Simple image filters" project.
# For details, see https://github.com/egor-tensin/filters.
# Distributed under the MIT License.

import argparse
import sys

import cv2
import numpy as np

def gen_kernel(radius):
    size = radius * 2 + 1
    return np.ones((size, size)) / size ** 2

def convolve(img, kernel):
    #print(kernel)
    radius = kernel.shape[0] // 2
    output = np.zeros(img.shape, dtype=img.dtype)
    for i in range(radius, img.shape[0] - radius):
        for j in range(radius, img.shape[1] - radius):
            neighborhood = img[i - radius:i + radius + 1, j - radius:j + radius + 1]
            output[i, j] = np.sum(kernel * neighborhood)
    return output

DEFAULT_RADIUS = 1

def mean(img_path, radius=DEFAULT_RADIUS, output_path=None):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    kernel = gen_kernel(radius)
    output = convolve(img, kernel)
    if output_path is None:
        cv2.imshow("Output", output)
        cv2.waitKey()
    else:
        cv2.imwrite(output_path, output)

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
    parser.add_argument('--radius', '-r',
                        type=_parse_non_negative_integer,
                        default=DEFAULT_RADIUS)
    return parser.parse_args(args[1:])

def main(args=sys.argv):
    mean(**vars(_parse_args(args)))

if __name__ == '__main__':
    main()
