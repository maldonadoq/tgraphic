import numpy as np
import cv2 as cv
import sys

sys.path.append('src/')
from utils import *

if __name__ == "__main__":
    img = cv.imread('input/3.png', 0)

    #cv.imshow('Normal', img)

    tsobel(img)

    cv.waitKey()
    cv.destroyAllWindows()