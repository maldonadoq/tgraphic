import numpy as np
import cv2 as cv
import sys

sys.path.append('src/')
from utils import *

if __name__ == "__main__":

    img_name = 'input/cell_img/4.png'
    truth_name = 'input/cell_truth/4.png'

    if (len(sys.argv) == 3):
        img_name = sys.argv[1]
        truth_name = sys.argv[2]

    img = cv.imread(img_name, 0)
    truth = cv.imread(truth_name, 0)

    '''
        1 = Sobel
        2 = Prewit
    '''

    s = mfilter(img,1)
    t = mthreshold(s)
    w = mwatershed(t)

    ss = mssim(w, truth)
    print('SSIM: ', ss)

    cv.imshow('Watershed - Truth', np.concatenate((w, truth), axis=1))

    cv.waitKey()
    cv.destroyAllWindows()