import numpy as np
import cv2 as cv
import sys

sys.path.append('src/')
from utils import *

def blur(src, a, t):
    rows, cols = src.shape[:2]
    img = np.zeros(src.shape)

    a = a//2
    for i in range(a, rows - a):
        rt0 = i - a
        rt1 = i + a + 1
        for j in range(a, cols - a):
            ct0 = j - a
            ct1 = j + a + 1
            window = src[rt0:rt1, ct0:ct1]
            if(window.sum() > t):
                img[i,j] = 1
    return img

if __name__ == "__main__":

    img_name = 'input/cell_img/7.png'
    if (len(sys.argv) == 2):
        img_name = sys.argv[1]

    img = cv.imread(img_name, 0)

    s = mfilter(img)
    t = mthreshold(s)
    w = mwatershed(t)

    b = blur(w,3,7)
    wb = mwatershed(b)

    cv.imwrite('input/cell_truth/7.png', wb)
    cv.waitKey()
    cv.destroyAllWindows()