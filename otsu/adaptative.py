import numpy as np
import cv2 as cv
import sys

sys.path.append('src/')

from utils import *

if __name__ == "__main__":
    
    name = '../images/input/casa.png'
    n = 2
    
    if(len(sys.argv) == 2):
        n = int(sys.argv[1])
    elif(len(sys.argv) == 3):
        n = int(sys.argv[1])
        name = sys.argv[2]

    img = cv.imread(name, 0)
    thr = adaptative_otsu(img, n)
    
    cv.imshow('Normal', img)
    cv.imshow('Otsu', thr)

    cv.waitKey()
    cv.destroyAllWindows()