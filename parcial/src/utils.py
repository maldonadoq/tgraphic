from skimage.morphology import watershed
from skimage.feature import peak_local_max
from skimage.metrics import structural_similarity as ssim
from scipy import ndimage as ndi

import numpy as np
import cv2 as cv

# Normalize into 0-255
def mnormalize(src):
    img = np.zeros(src.shape, dtype="uint8")
    tmin = src.min()
    tmax = src.max()
    nmax = abs(tmax - tmin)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            nv = ((src[i,j] - tmin) * 255)/nmax
            img[i,j] = nv

    return img


def mboundary(src):
    img = np.zeros(src.shape, dtype="uint8")

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if(src[i,j] > 0):
                img[i,j] = 255

    return img

def mpadding(shape):
    hx = np.zeros(shape)
    hy = np.zeros(shape)

    cx = shape[0]//2
    cy = shape[1]//2

    hx[cx-1:cx+2, cy-1:cy+2] = np.array([[-1,0,1], [-2,0,2], [-1,0,1]])
    hy[cx-1:cx+2, cy-1:cy+2] = np.array([[1,2,1], [0,0,0], [-1,-2,-1]])

    return (hx,hy)

def msobel(src):
	# To Frequency Domain
    X = np.fft.fft2(src)
    h = mpadding(src.shape)

    Hx = np.fft.fft2(np.fft.fftshift(h[0]))
    Hy = np.fft.fft2(np.fft.fftshift(h[1]))

    fx = np.abs(np.fft.ifft2(X * Hx))
    fy = np.abs(np.fft.ifft2(X * Hy))

    S = np.sqrt((fx*fx) + (fy*fy))
    return S

def mthreshold(src):
    ret, T = cv.threshold(src, 120, 255, cv.THRESH_BINARY)
    return T

def mwatershed(src):
    dist = ndi.distance_transform_edt(src)
    local_maxi = peak_local_max(dist, indices=False, footprint=np.ones((3, 3)),
                                labels=src)
    markers = ndi.label(local_maxi)[0]
    labels = watershed(-dist, markers, mask=src)

    return mboundary(markers)

def mssim(src, truth):
    tssim = ssim(src, truth, data_range=src.max() - src.min())
    return tssim