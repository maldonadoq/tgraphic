from math import (ceil, log)
import numpy as np
import cv2 as cv

import sys

sys.path.append('src/')
from utils import *
from fast import mfourier_filter, mfast_fourier

if __name__ == "__main__":
    img = cv.imread('../images/input/aa.png', 0)
    img = cv.resize(img, (300,300))

    dft = mfast_fourier(img)
    shape = dft[0].shape

    X = mnormalize(mlog(np.abs(mshift(dft[0]))) ** 2)
    X = cv.resize(X, img.shape)
    cv.imshow('Fast Fourier Transform', X)

    d0 = 150

    tf = 'l'
    if (len(sys.argv) == 2):
        tf = sys.argv[1]

    if (tf == 'l'):
        kil = mfilter(shape, mideal_lowpass, d0)
        kbl = mfilter(shape, mbutterworth_lowpass, d0)
        kgl = mfilter(shape, mgaussian_lowpass, d0)

        mfourier_filter(dft, img.shape, kil, "Ideal Low-Pass")
        mfourier_filter(dft, img.shape, kbl, "ButterWorth Low-Pass")
        mfourier_filter(dft, img.shape, kgl, "Gaussian Low-Pass")
    elif (tf == 'h'):
        kih = mfilter(shape, mideal_highpass, d0)
        kbh = mfilter(shape, mbutterworth_highpass, d0)
        kgh = mfilter(shape, mgaussian_highpass, d0)

        mfourier_filter(dft, img.shape, kih, "Ideal High-Pass")
        mfourier_filter(dft, img.shape, kbh, "ButterWorth High-Pass")
        mfourier_filter(dft, img.shape, kgh, "Gaussian High-Pass")
    else:
        print("You should run in this case: python name.py [l|h]")

    cv.waitKey()
    cv.destroyAllWindows()