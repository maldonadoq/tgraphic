import numpy as np
import cv2 as cv
import sys

sys.path.append('src/')
from filter import lfilter, mfilter

def mmedia(window):
    return round(window.sum() / window.size)

def mmedian(window):
    mlist = sorted(window.flatten())
    idx = len(mlist)//2
    return mlist[idx]

def mmin(window):
    return window.min()

def mmax(window):
    return window.max()

def gauss_kernel(wsize, sigma):
    if(wsize%2 == 0):
        wsize += 1

    kernel = np.zeros((wsize, wsize), float)
    step = wsize//2
    
    ds = 2*pow(sigma,2)
    const = 1/(ds*np.pi)

    for i in range(-step, step+1):
        for j in range(-step, step+1):
            kernel[i+step, j+step] = const*np.exp(-((pow(i,2) + pow(j,2))/ds))

    tmin = kernel.min()
    return kernel//tmin

if __name__ == "__main__":
    img = cv.imread('../images/input/lena.jpg', 0)

    window_size = 3

    # Lineal and Estadistic Filters
    tmedia  = lfilter(img, window_size, mmedia)
    tmedian = lfilter(img, window_size, mmedian)
    tmin    = lfilter(img, window_size, mmin)
    tmax    = lfilter(img, window_size, mmax)

    hgauss   = gauss_kernel(window_size,0.8)
    tgauss   = mfilter(img, hgauss)

    cv.imwrite('../images/output/media.jpg', tmedia)
    cv.imwrite('../images/output/mediana.jpg', tmedian)
    cv.imwrite('../images/output/min.jpg', tmin)
    cv.imwrite('../images/output/max.jpg', tmax)
    cv.imwrite('../images/output/gauss.jpg', tgauss)

    cv.imshow('Normal', img)
    cv.imshow('Media', tmedia)
    cv.imshow('Mediana', tmedian)
    cv.imshow('Minimo', tmin)
    cv.imshow('Máximo', tmax)
    cv.imshow('Gauss', tgauss)

    cv.waitKey()
    cv.destroyAllWindows()