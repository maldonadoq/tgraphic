import numpy as np
import cv2 as cv
import sys

sys.path.append('src/')

from utils import *

if __name__ == "__main__":
    
    img = cv.imread('../images/input/casa.png', 0)
    n = 2
    
    if(len(sys.argv) == 2):
        n = int(sys.argv[1])

    thr = adaptative_otsu(img, n)
    
    cv.imshow('Normal', img)
    cv.imshow('Otsu', thr)

    cv.waitKey()
    cv.destroyAllWindows()