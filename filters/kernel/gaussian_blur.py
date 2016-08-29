# Copyright 2016 (c) Egor Tensin <Egor.Tensin@gmail.com>
# This file is part of the "Simple image filters" project.
# For details, see https://github.com/egor-tensin/filters.
# Distributed under the MIT License.

import numpy as np

def gen_kernel(radius, sigma):
    kernel = np.array([[i ** 2 + j ** 2
        for i in range(-radius, radius + 1)]
        for j in range(-radius, radius + 1)])
    kernel = -kernel / (2 * sigma ** 2)
    kernel = np.exp(kernel)
    kernel = kernel / np.sum(kernel)
    return kernel
