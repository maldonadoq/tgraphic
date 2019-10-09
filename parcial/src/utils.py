import numpy as np
import cv2 as cv

# Normalize into 0-255
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

# Applying Sobel Filter
def tfilter(src):
    src_out = np.zeros(src.shape, src.dtype)
    rows, cols = src.shape[:2]

    sx = np.array([[-1,0,1], [-2,0,2], [-1,0,1]])
    sy = np.array([[1,2,1], [0,0,0], [-1,-2,-1]])

    fsx = np.fft.fft2(sx)
    fsy = np.fft.fft2(sy)

    #fsx = np.fft.fftshift( np.fft.fft2(sx) )
    #fsy = np.fft.fftshift( np.fft.fft2(sy) )
    
    step = 1

    for i in range(step, rows - step):
        rt0 = i - step
        rt1 = i + step + 1
        for j in range(step, cols - step):
            ct0 = j - step
            ct1 = j + step + 1
            window = src[rt0:rt1, ct0:ct1]
            
            hx = (window*sx).sum()
            hy = (window*sy).sum()

            src_out[i,j] = hx + hy
            
    return src_out

def tsobel(x):
	# To Frequency Domain
	X = np.fft.fft2(x)
	#X = np.fft.fftshift(X)

	# Sobel Filter in FD
	fX = tfilter(X)

	# to Spatial Domain
	#x = np.fft.ifftshift(fX)
	x = np.fft.ifft2(fX)
	x = np.abs(x)
	x = mnormalize(x)

	cv.imshow('Filter', x)