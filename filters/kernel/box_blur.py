# Copyright 2016 (c) Egor Tensin <Egor.Tensin@gmail.com>
# This file is part of the "Simple image filters" project.
# For details, see https://github.com/egor-tensin/filters.
# Distributed under the MIT License.

import numpy as np

def gen_kernel(radius):
    size = radius * 2 + 1
    return np.ones((size, size)) / size ** 2
