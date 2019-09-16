import numpy as np
import cv2 as cv
import sys

sys.path.append('src/')
from filter import mfilter, nfilter

if __name__ == "__main__":
    img = cv.imread('../images/input/coins.png', 0)

    hlaplace = np.array([[0,1,0], [1,-4,1], [0,1,0]])
    hxrobert = np.array([[-1,0,0], [0,1,0], [0,0,0]])
    hyrobert = np.array([[0,-1,0], [1,0,0], [0,0,0]])
    hxsobel  = np.array([[-1,0,1], [-2,0,2], [-1,0,1]])
    hysobel  = np.array([[-1,-2,-1], [0,0,0], [1,2,1]])
    hxprewit = np.array([[1,0,-1], [1,0,-1], [1,0,-1]])
    hyprewit = np.array([[1,1,1], [0,0,0], [-1,-1,-1]])

    tlaplace = mfilter(img, hlaplace)
    trobert  = nfilter(img, hxrobert, hyrobert)
    tsobel   = nfilter(img, hxsobel, hysobel)
    tprewitt = nfilter(img, hxprewit, hyprewit)

    cv.imwrite('../images/output/laplace.jpg', tlaplace)
    cv.imwrite('../images/output/robert.jpg', trobert)
    cv.imwrite('../images/output/sobel.jpg', tsobel)
    cv.imwrite('../images/output/prewitt.jpg', tprewitt)

    cv.imshow('Normal', img)
    cv.imshow('Laplace', tlaplace)
    cv.imshow('Robert', trobert)
    cv.imshow('Sobel', tsobel)
    cv.imshow('Prewitt', tprewitt)

    cv.waitKey()
    cv.destroyAllWindows()