import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
import sys

sys.path.append('src/')

from utils import *

if __name__ == "__main__":
    
    name = '../images/input/casa.png'
    n = 4
    if(len(sys.argv) == 2):
        n = int(sys.argv[1])
    elif(len(sys.argv) == 3):
        n = int(sys.argv[1])
        name = sys.argv[2]

    if(n < 4):
        n = 4

    img = cv.imread(name, 0)

    ts = multi_threshold(img, n)
    sg = segmentation(img, ts)

    cv.imshow('Normal', img)
    cv.imshow('Segmentation', sg)

    cv.waitKey()
    cv.destroyAllWindows()