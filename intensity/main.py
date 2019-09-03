from math import (cos, sin, radians, floor, ceil, log, pow)
import numpy as np
import cv2 as cv

@np.vectorize
def mlogarithm(x, c = 1):
	return (c*log(x/255 + 1, 2))*255

"""@np.vectorize
def mlogarithm_inverse(x, c = 1):
	return pow(2, x/(255*c))*255"""

def mlogarithm_inverse(img_in, c = 1):
    shape = img_in.shape
    img_out = np.empty(shape, img_in.dtype)

    for i in range(shape[0]):
        for j in range(shape[1]):
            img_out[i, j] = (pow(2, img_in[i, j]/(255*c)))*255

    return img_out

@np.vectorize
def mpower(x, gamma, eps = 0, c = 1):
	return (c*pow(x/255 + eps, gamma))*255

@np.vectorize
def mnegative(x):
    return 255 - x

if __name__ == "__main__":
    img = cv.imread('../images/input/lena.jpg', 0)

    tlog      = mlogarithm(img)
    tloginve  = mlogarithm_inverse(img)
    tpow 	  = mpower(img, 2)
    tneg  	  = mnegative(img)

    cv.imwrite('../images/output/logaritmo.jpg', tlog)
    cv.imwrite('../images/output/logaritmo_inverso.jpg', tloginve)
    cv.imwrite('../images/output/power.jpg', tpow)
    cv.imwrite('../images/output/negative.jpg', tneg)

    """cv.imshow('Logarithm', tlog)
    cv.imshow('Inverse Logarithm', tloginve)
    cv.imshow('Power', tpow)
    #cv.imshow('Negative', tneg)
    cv.waitKey()
    cv.destroyAllWindows()"""