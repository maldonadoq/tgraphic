from math import (pow, sqrt, exp)
import numpy as np

#Smoothin

def mdistance(a, b):
	return sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2))

def mideal_lowpass(dist, d0, n):
	res = 0
	if(dist <= d0):
		res = 1
	return res

def mbutterworth_lowpass(dist, d0, n):
	return 1/(1 + pow(dist/d0, 2*n))

def mgaussian_lowpass(dist, d0, n):
	return exp(-pow(dist,2)/(2*pow(d0,2)))

#Border

def mideal_highpass(dist, d0, n):
	res = 1
	if(dist <= d0):
		res = 0
	return res

def mbutterworth_highpass(dist, d0, n):
	if(dist == 0.0):
		dist = 0.001
	return 1/(1 + pow(d0/dist, 2*n))

def mgaussian_highpass(dist, d0, n):
	return 1-exp(-pow(dist,2)/(2*pow(d0,2)))

#Create Filter

def mfilter(shape, op,  d0, on = 2):
	tfilter = np.zeros(shape, float)
	center = (shape[0]//2, shape[1]//2)

	dist = 0.0
	for i in range(shape[0]):
		for j in range(shape[1]):
			dist = mdistance((i,j), center)
			tfilter[i,j] = op(dist, d0, on)

	return tfilter

#Image Double and Half
def mimg_double(img_in):
	rows, cols = img_in.shape[:2]
	img_out = np.zeros((rows*2, cols*2), img_in.dtype)

	img_out[0:rows, 0:cols] = img_in
	return img_out

def mimg_half(img_in):
	rows, cols = (img_in.shape[0]//2, img_in.shape[1]//2)
	img_out = np.zeros((rows, cols), img_in.dtype)

	img_out = img_in[0:rows, 0:cols]
	return img_out

# Normalize
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

def mto_float(img_in):
    img_out = np.zeros(img_in.shape, float)
    for i in range(img_out.shape[0]):
        for j in range(img_out.shape[1]):
        	img_out[i,j] = abs(img_in[i,j])

    return img_out

def mprint(img):
	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			#print("%2.2f"%img[i,j], end = ' ')
			print(img[i,j], end = ' ')
		print()
	print('\n')

@np.vectorize
def mlog(x):
	if(x == 0):
		x = 0.0000000001
	return np.log(x)