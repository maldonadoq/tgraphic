import numpy as np
import cv2 as cv
import sys

sys.path.append('src/')
from utils import *

'''
Python 3
    1) python main.py input/cell_img/1.png input/cell_truth/1.png
    2) python main.py 1
'''

if __name__ == "__main__":

    dt = 1
    '''
        1 = Frequency Sobel
        2 = Sobel
        3 = Prewit
        4 = Robert
        5 = Laplace
    '''

    img_name = 'input/cell_img/4.png'
    truth_name = 'input/cell_truth/4.png'

    sz = len(sys.argv)
    if(sz == 2):
        dt = int(sys.argv[1])
    elif (len(sys.argv) == 3):
        img_name = sys.argv[1]
        truth_name = sys.argv[2]

    img = cv.imread(img_name, 0)
    truth = cv.imread(truth_name, 0)

    s = mfilter(img,dt)
    t = mthreshold(s)
    w = mwatershed(t)

    ss = mssim(w, truth)
    print('SSIM: ', ss)

    cv.imshow('Filter - Threshold', np.concatenate((mnormalize(s),mnormalize(t)), axis=1))
    cv.imshow('Watershed - Truth', np.concatenate((w,truth), axis=1))

    cv.waitKey()
    cv.destroyAllWindows()