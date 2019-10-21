import numpy as np
from math import sqrt, pow

def filter1(src, hfilter):
    rows, cols = src.shape[:2]
    img = np.zeros(src.shape)

    step = 1

    for i in range(step, rows - step):
        rt0 = i - step
        rt1 = i + step + 1
        for j in range(step, cols - step):
            ct0 = j - step
            ct1 = j + step + 1
            window = src[rt0:rt1, ct0:ct1]
            img[i,j] = abs((window * hfilter).sum())
            
    return img

def filter2(src, xfilter, yfilter):
    img = np.zeros(src.shape)
    rows, cols = src.shape[:2]
    
    step = 1

    for i in range(step, rows - step):
        rt0 = i - step
        rt1 = i + step + 1
        for j in range(step, cols - step):
            ct0 = j - step
            ct1 = j + step + 1
            window = src[rt0:rt1, ct0:ct1]
            hx = (window*xfilter).sum()
            hy = (window*yfilter).sum()
            img[i,j] = sqrt(pow(hx,2) + pow(hy,2))

    return img