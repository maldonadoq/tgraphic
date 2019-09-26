from math import (ceil, log)
import numpy as np
import cv2 as cv

import sys

sys.path.append('src/')
from utils import *
from fast import mfourier

if __name__ == "__main__":
    img = cv.imread('../images/input/lena.jpg', 0)
    shape = (2 ** ceil(log(img.shape[0], 2)), 2 ** ceil(log(img.shape[1], 2)))

    d0 = 100

    kil = mfilter(shape, mideal_lowpass, d0)
    kbl = mfilter(shape, mbutterworth_lowpass, d0)
    kgl = mfilter(shape, mgaussian_lowpass, d0, 0.7)

    kih = mfilter(shape, mideal_highpass, d0)
    kbh = mfilter(shape, mbutterworth_highpass, d0)
    kgh = mfilter(shape, mgaussian_highpass, d0, 0.7)

    mfourier(img, kil, "Ideal Low-Pass")
    mfourier(img, kbl, "ButterWorth Low-Pass")
    mfourier(img, kgl, "Gaussian Low-Pass")

    mfourier(img, kih, "Ideal High-Pass")
    mfourier(img, kbh, "ButterWorth High-Pass")
    mfourier(img, kgh, "Gaussian High-Pass")

    cv.waitKey()
    cv.destroyAllWindows()