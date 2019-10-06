import numpy as np
import cv2 as cv

import sys

sys.path.append('src/')
from utils import *

def trgb(img):
	r,g,b = rgb(img)

	tmp = np.concatenate((r, g, b), axis=1)
	cv.imshow('RGB', tmp)

def trgb_to_cmy(img):
	c,m,y = rgb_to_cmy(img)

	tmp = np.concatenate((c, m, y), axis=1)
	cv.imshow('RGB -> CMY', tmp)

def trgb_to_hsv(img):
	h,s,v = rgb_to_hsv(img)

	tmp = np.concatenate((h, s, v), axis=1)
	cv.imshow('RGB -> HSV', tmp)

def trgb_to_hsi(img):
	h,s,i = rgb_to_hsi(img)

	tmp = np.concatenate((h, s, i), axis=1)
	cv.imshow('RGB -> HSI', tmp)

def trgb_to_yuv(img):
	y,u,v = rgb_to_yuv(img)

	tmp = np.concatenate((y, u, v), axis=1)
	cv.imshow('RGB -> YUV', tmp)

def trgb_to_yiq(img):
	y,i,q = rgb_to_yiq(img)

	tmp = np.concatenate((y, i, q), axis=1)
	cv.imshow('RGB -> YIQ', tmp)

def trgb_to_ycbcr(img):
	y,cb,cr = rgb_to_ycbcr(img)

	tmp = np.concatenate((y, cb, cr), axis=1)
	cv.imshow('RGB -> YCbCr', tmp)

if __name__ == "__main__":
	img = cv.imread('../images/input/lena.jpg')

	#trgb(img)
	#trgb_to_cmy(img)
	trgb_to_hsv(img)
	trgb_to_hsi(img)
	#trgb_to_yuv(img)
	#trgb_to_yiq(img)
	#trgb_to_ycbcr(img)

	cv.waitKey()
	cv.destroyAllWindows()