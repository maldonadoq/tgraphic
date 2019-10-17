import numpy as np
import cv2 as cv
import sys

sys.path.append('src/')
from utils import *

if __name__ == "__main__":
    img = cv.imread('input/4.png', 0)
    
    s = msobel(img)
    t = mthreshold(s)
    w = mwatershed(t)
    ss = mssim(w)

    cv.imshow('Sobel', mnormalize(s))
    cv.imshow('Threshold', t)
    cv.imshow('Watershed', w)
    print('SSMI: ' + str(ss))

    cv.imwrite('output/Sobel.jpg', s)
    cv.imwrite('output/Threshold.jpg', mnormalize(t))
    cv.imwrite('output/Watershed.jpg', w)

    cv.waitKey()
    cv.destroyAllWindows()