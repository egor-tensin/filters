# Copyright 2016 (c) Egor Tensin <Egor.Tensin@gmail.com>
# This file is part of the "Simple image filters" project.
# For details, see https://github.com/egor-tensin/filters.
# Distributed under the MIT License.

import cv2

def load_grayscale(path):
    return cv2.imread(path, cv2.IMREAD_GRAYSCALE)

def save(path, img):
    cv2.imwrite(path, img)

def show(img, window_title=None):
    cv2.imshow(window_title, img)
    cv2.waitKey()
