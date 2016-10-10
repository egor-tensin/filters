# Copyright 2016 (c) Egor Tensin <Egor.Tensin@gmail.com>
# This file is part of the "Simple image filters" project.
# For details, see https://github.com/egor-tensin/filters.
# Distributed under the MIT License.

import argparse

def parse_non_negative_integer(src):
    try:
        n = int(src)
    except ValueError:
        raise argparse.ArgumentTypeError('must be a non-negative integer: ' + src)
    if n < 0:
        raise argparse.ArgumentTypeError('must be a non-negative integer: ' + src)
    return n
