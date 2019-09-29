import cmath
import cv2 as cv
import numpy as np
from math import (log, ceil)
from utils import mnormalize, mlog, mshift

def mfourier_filter(fft, tshape, tfilter, name = "Fast Fourier Transform"):	
	tfft, m, n = fft
	tfft = tfft * tfilter
	tifft = mifast_fourier(tfft, m, n)

	tX = mnormalize(mlog(np.abs(mshift(tfft))) ** 2)
	X = cv.resize(tX, tshape)

	x = mnormalize(np.abs(tifft))

	img_out = np.concatenate((X, x), axis=1)
	cv.imshow(name, img_out)

'''FFT of 2-d Images with padding usage X, m, n = mfast_fourier(x)'''
def mfast_fourier(f):
	f, m, n = mpadding(f)

	return np.transpose(mfft(np.transpose(mfft(f)))), m, n

''' IFFT of 2-d signals usage x = ifft2(X, m, n)'''
def mifast_fourier(F, m, n):
	f, M, N = mfast_fourier(np.conj(F))
	f = np.matrix(np.real(np.conj(f))) / (M*N)

	return f[:m, :n]

def mpadding(f):
	m, n = f.shape
	M, N = 2 ** ceil(log(m, 2)), 2 ** ceil(log(n, 2))
	F = np.zeros((M,N), dtype = f.dtype)
	F[0:m, 0:n] = f

	return F, m, n

''' FFT of 1-d signals usage : X = fft(x)'''
def mfft(x):
	n = len(x)
	if(n == 1):
		return x

	Feven, Fodd = mfft(x[0::2]), mfft(x[1::2])
	combined = [0] * n

	mid = n//2
	for m in range(mid):
		combined[m] = Feven[m] + omega(n, -m) * Fodd[m]
		combined[m + mid] = Feven[m] - omega(n, -m) * Fodd[m]

	return combined

''' The omega term in DFT and IDFT formulas'''
def omega(p, q):
   return cmath.exp((2.0 * cmath.pi * 1j * q) / p)