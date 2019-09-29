import cv2 as cv
import numpy as np
from utils import mnormalize, mlog, mshift

class DiscreteFourier(object):
	def __init__(self):
		self.f = None
		self.F = None
		self.image = None

	def set(self, _image):
		self.image = _image

	def forward(self):
		M = self.image.shape[0]
		N = self.image.shape[1]

		x = np.arange(M, dtype = float)
		y = np.arange(N, dtype = float)

		u = x.reshape((M,1))
		v = y.reshape((N,1))

		exp1 = pow(np.e, -(2j * np.pi * u * x)/M)
		exp2 = pow(np.e, -(2j * np.pi * v * y)/N)

		self.F = np.dot(exp2, np.dot(exp1, self.image).transpose())/(M*N)
		return self.F

	def dft(self):
		ft = mlog(np.abs(mshift(self.forward())) ** 2)
		cv.imshow("Discrete Fourier Transform", mnormalize(ft))

	def idft(self, I):
		M = I.shape[0]
		N = I.shape[1]

		x = np.arange(M, dtype = float)
		y = np.arange(N, dtype = float)

		u = x.reshape((M,1))
		v = y.reshape((N,1))

		exp1 = pow(np.e, (2j * np.pi * u * x)/M)
		exp2 = pow(np.e, (2j * np.pi * v * y)/N)

		self.f = np.dot(exp2, np.dot(exp1, I).transpose())
		return self.f

	def filter(self, _filter, _name = "Ideal Low-Pass"):
		X = self.F * _filter
		tdft = mlog(np.abs(mshift(X)) ** 2)

		x = self.idft(X)
		tidft = np.abs(x)

		img = np.concatenate((mnormalize(tdft), mnormalize(tidft)), axis=1)
		cv.imshow(_name, img)