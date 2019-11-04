import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

import sys

sys.path.append('src/')

from utils import *

if __name__ == "__main__":
    
    img = cv.imread('../images/input/coins.png', 0)
    plt.figure(1)
    plt.imshow(img, 'gray')
    plt.title('Normal')


    hist = histogram(img)
    plt.figure(2)
    plt.bar(np.arange(256), hist)
    plt.title('Histogram')


    t = otsu_threshold(img, hist)
    seg = segmentation(img, t)
    plt.figure(3)
    plt.imshow(seg, 'gray')
    plt.title('Segmentation')

    plt.show()