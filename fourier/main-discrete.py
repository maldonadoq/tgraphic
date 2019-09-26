import numpy as np
import cv2 as cv

import sys

sys.path.append('src/')
from utils import *
from discrete import DiscreteFourier

if __name__ == "__main__":
    img = cv.imread('../images/input/lena.jpg', 0)
    
    shape = img.shape
    d0 = 50

    fourier = DiscreteFourier()
    fourier.set(img)
    fourier.dft()

    kil = mfilter(shape, mideal_lowpass, d0)
    kbl = mfilter(shape, mbutterworth_lowpass, d0)

    kih = mfilter(shape, mideal_highpass, d0)
    kbh = mfilter(shape, mbutterworth_highpass, d0)

    #fourier.filter(kbl, "ButterWorth Low-Pass")
    fourier.filter(kbh, "ButterWorth High-Pass")

    cv.waitKey()
    cv.destroyAllWindows()