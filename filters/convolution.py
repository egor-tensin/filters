# Copyright 2016 (c) Egor Tensin <Egor.Tensin@gmail.com>
# This file is part of the "Simple image filters" project.
# For details, see https://github.com/egor-tensin/filters.
# Distributed under the MIT License.

import numpy as np

def convolve(img, kernel):
    #print(kernel)
    radius = kernel.shape[0] // 2
    output = np.zeros(img.shape, dtype=img.dtype)
    for i in range(radius, img.shape[0] - radius):
        for j in range(radius, img.shape[1] - radius):
            neighborhood = img[i - radius:i + radius + 1, j - radius:j + radius + 1]
            output[i, j] = np.sum(neighborhood * kernel)
    return output
