import numpy as np
import cv2 as cv
import sys

sys.path.append('src/')
from utils import *

if __name__ == "__main__":

    img_path = 'input/cell_img'
    truth_path = 'input/cell_truth'

    img_name = mimgs(img_path)
    truth_name = mimgs(truth_path)

    dt = 1
    if (len(sys.argv) == 2):
        dt = int(sys.argv[1])

    number = len(img_name)
    avg = 0
    for i in range(number):
        img = cv.imread(img_name[i], 0)
        truth = cv.imread(truth_name[i], 0)

        s = mfilter(img, dt)
        t = mthreshold(s)
        w = mwatershed(t)
        ss = mssim(w, truth)

        #print ('SSIM: ', ss)
        avg += ss

    print('AVG SSIM: ', avg/number)