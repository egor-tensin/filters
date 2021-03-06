# Copyright 2016 (c) Egor Tensin <Egor.Tensin@gmail.com>
# This file is part of the "Simple image filters" project.
# For details, see https://github.com/egor-tensin/filters.
# Distributed under the MIT License.

from enum import Enum

import numpy as np

class Direction(Enum):
    NORTH = 'N'
    NORTH_EAST = 'NE'
    NORTH_WEST = 'NW'
    SOUTH = 'S'
    SOUTH_EAST = 'SE'
    SOUTH_WEST = 'SW'
    EAST = 'E'
    WEST = 'W'

    def gen_kernel(self, distance):
        radius = distance
        r = radius
        size = 2 * radius + 1
        kernel = np.zeros((size, size))

        if   self is Direction.NORTH:      x, y = -1,  r
        elif self is Direction.NORTH_EAST: x, y = -1,  0
        elif self is Direction.EAST:       x, y =  r,  0
        elif self is Direction.SOUTH_EAST: x, y =  0,  0
        elif self is Direction.SOUTH:      x, y =  0,  r
        elif self is Direction.SOUTH_WEST: x, y =  0, -1
        elif self is Direction.WEST:       x, y =  r, -1
        elif self is Direction.NORTH_WEST: x, y = -1, -1
        else:
            raise NotImplementedError('unsupported direction: ' + str(self))

        kernel[x, y] = 1
        return kernel

    def __str__(self):
        return self.value
