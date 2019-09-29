import numpy as np
import cv2 as cv

import sys

sys.path.append('src/')
from utils import *
from discrete import DiscreteFourier

if __name__ == "__main__":
    shape = (300, 300)
    img = cv.imread('../images/input/aa.png', 0)
    img = cv.resize(img, shape)
    
    d0 = 100

    fourier = DiscreteFourier()
    fourier.set(img)
    fourier.dft()

    tf = 'l'
    if (len(sys.argv) == 2):
        tf = sys.argv[1]

    if (tf == 'l'):
        kil = mfilter(shape, mideal_lowpass, d0)
        kbl = mfilter(shape, mbutterworth_lowpass, d0)
        kgl = mfilter(shape, mgaussian_lowpass, d0)

        fourier.filter(kil, "Ideal Low-Pass")
        fourier.filter(kbl, "ButterWorth Low-Pass")
        fourier.filter(kgl, "Gaussian Low-Pass")
    elif (tf == 'h'):
        kih = mfilter(shape, mideal_highpass, d0)
        kbh = mfilter(shape, mbutterworth_highpass, d0)
        kgh = mfilter(shape, mgaussian_highpass, d0)

        fourier.filter(kih, "Ideal High-Pass")
        fourier.filter(kbh, "ButterWorth High-Pass")
        fourier.filter(kgh, "Gaussian High-Pass")
    else:
        print("You should run in this case: python name.py [l|h]")

    cv.waitKey()
    cv.destroyAllWindows()