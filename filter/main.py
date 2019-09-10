from math import (ceil)
import numpy as np
import cv2 as cv

# Lineal and Estadistic Filters
def lfilter(img_in, wsize, op):
    rows = img_in.shape[0]
    cols = img_in.shape[1]

    img_out = np.zeros(img_in.shape, img_in.dtype)
    step = wsize//2

    for i in range(step, rows - step):
        rt0 = i - step
        rt1 = i + step + 1
        for j in range(step, cols - step):
            ct0 = j - step
            ct1 = j + step + 1
            window = img_in[rt0:rt1, ct0:ct1]
            img_out[i,j] = op(window)

    return img_out

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

def mnormalize(img_in):
    img_out = np.zeros(img_in.shape, dtype="uint8")
    tmin = img_in.min()
    tmax = img_in.max()
    nmax = abs(tmax - tmin)

    for i in range(img_out.shape[0]):
        for j in range(img_out.shape[1]):
            nv = ((img_in[i,j] - tmin) * 255)/nmax
            img_out[i,j] = nv

    return img_out

# Filters with only one mask (Laplace)
def mfilter(img_in, hfilter):
    img_out = np.zeros(img_in.shape, int)
    rows = img_in.shape[0]
    cols = img_in.shape[1]

    if(hfilter.shape[0] != hfilter.shape[1]):
        print("The shape would be a square!")
        return img_out
    
    wsize = hfilter.shape[0]
    step = wsize//2

    for i in range(step, rows - step):
        rt0 = i - step
        rt1 = i + step + 1
        for j in range(step, cols - step):
            ct0 = j - step
            ct1 = j + step + 1
            window = img_in[rt0:rt1, ct0:ct1]
            nv = (window * hfilter).sum()
            img_out[i,j] = nv
            
    return mnormalize(img_out)

# Filters with two mask (Robert, Sobel, Prebits)
def nfilter(img_in, xfilter, yfilter):
    img_out = np.zeros(img_in.shape, int)
    rows = img_in.shape[0]
    cols = img_in.shape[1]

    if((xfilter.shape != yfilter.shape) and (xfilter.shape[0] != xfilter.shape[1])):
        print("both matrix would be same shape and shape would be a square!")
        return img_out
    
    wsize = xfilter.shape[0]
    step = wsize//2

    for i in range(step, rows - step):
        rt0 = i - step
        rt1 = i + step + 1
        for j in range(step, cols - step):
            ct0 = j - step
            ct1 = j + step + 1
            window = img_in[rt0:rt1, ct0:ct1]
            hx = (window*xfilter).sum()
            hy = (window*yfilter).sum()

            img_out[i,j] = hx + hy

    return mnormalize(img_out)


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
    img = cv.imread('../images/input/coins.png', 0)

    window_size = 3

    # Lineal and Estadistic Filters
    #tmedia  = lfilter(img, window_size, mmedia)
    #tmedian = lfilter(img, window_size, mmedian)
    #tmin    = lfilter(img, window_size, mmin)
    #tmax    = lfilter(img, window_size, mmax)

    hlaplace = np.array([[0,1,0], [1,-4,1], [0,1,0]])
    hxrobert = np.array([[-1,0,0], [0,1,0], [0,0,0]])
    hyrobert = np.array([[0,-1,0], [1,0,0], [0,0,0]])
    hxsobel  = np.array([[-1,0,1], [-2,0,2], [-1,0,1]])
    hysobel  = np.array([[-1,-2,-1], [0,0,0], [1,2,1]])

    hgauss   = gauss_kernel(3,0.8)

    tlaplace = mfilter(img, hlaplace)
    trobert  = nfilter(img, hxrobert, hyrobert)
    tsobel   = nfilter(img, hxsobel, hysobel)
    tgauss    = mfilter(img, hgauss)

    #cv.imwrite('../images/output/media.jpg', tmedia)
    #cv.imwrite('../images/output/mediana.jpg', tmedian)
    #cv.imwrite('../images/output/min.jpg', tmin)
    #cv.imwrite('../images/output/max.jpg', tmax)
    #cv.imwrite('../images/output/max.jpg', tmax)

    cv.imwrite('../images/output/laplace.jpg', tlaplace)
    cv.imwrite('../images/output/robert.jpg', trobert)
    cv.imwrite('../images/output/sobel.jpg', tsobel)
    cv.imwrite('../images/output/gauss.jpg', tgauss)

    #cv.imshow('Media', tmedia)
    #cv.imshow('Mediana', tmedian)
    #cv.imshow('Minimo', tmin)
    #cv.imshow('Máximo', tmax)

    cv.imshow('Laplace', tlaplace)
    cv.imshow('Robert', trobert)
    cv.imshow('Sobel', tsobel)
    cv.imshow('Gauss', tgauss)

    cv.waitKey()
    cv.destroyAllWindows()