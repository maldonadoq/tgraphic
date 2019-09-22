import numpy as np
import cv2 as cv
import sys

sys.path.append('src/')
from utils import *

def mfourier(img_in, tfilter):
    img_double = mimg_double(img_in)
    img_out = mimg_half(img_double)
   
    return img_out

if __name__ == "__main__":
    img = cv.imread('../images/input/lena.jpg', 0)

    shape = (5,5)
    kil = mfilter(shape, mideal_lowpass, 2)
    kbl = mfilter(shape, mbutterworth_lowpass, 3)
    kgl = mfilter(shape, mgaussian_lowpass, 3, 0.7)

    kih = mfilter(shape, mideal_highpass, 2)
    kbh = mfilter(shape, mbutterworth_highpass, 3)
    kgh = mfilter(shape, mgaussian_highpass, 3, 0.7)

    print(kil, "\n")
    print(kih)

    tfourier = mfourier(img, kil)
    cv.imshow('Fourier', tfourier)

    cv.waitKey()
    cv.destroyAllWindows()