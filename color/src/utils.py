import numpy as np
from math import sqrt, acos

def rgb(img):
	r = np.zeros(img.shape, img.dtype)
	g = np.zeros(img.shape, img.dtype)
	b = np.zeros(img.shape, img.dtype)

	r[:, :, 2] = img[:, :, 2]  # Red Channel
	g[:, :, 1] = img[:, :, 1]  # Green Channel
	b[:, :, 0] = img[:, :, 0]  # Blue Channel

	return r,g,b


def rgb_to_cmy(img):
	c = np.copy(img)
	m = np.copy(img)
	y = np.copy(img)

	c[:, :, 2] = 0  # Cian Channel
	m[:, :, 1] = 0  # Magenta Channel
	y[:, :, 0] = 0  # Yellow Channel

	return c,m,y

def rgb_to_cmyt(img):
	c = np.zeros(img.shape, img.dtype)
	m = np.zeros(img.shape, img.dtype)
	y = np.zeros(img.shape, img.dtype)

	c[:, :, 2] = 255 - img[:, :, 2]  # Cian Channel
	m[:, :, 1] = 255 - img[:, :, 1]  # Magenta Channel
	y[:, :, 0] = 255 - img[:, :, 0]  # Yellow Channel

	return c,m,y

def rgb_to_hsv(img):
	shape = img.shape[:2]
	h = np.zeros(shape)
	s = np.zeros(shape)
	v = np.zeros(shape)

	tmp = img/255
	for i in range(0, img.shape[0]):
		for j in range(0, img.shape[1]):
			px = tmp[i,j]
			b, g, r = px

			tmin = px.min()
			tmax = px.max()
			dist = tmax - tmin

			if(tmax == tmin):
				th = 0
			elif (tmax == r):
				th = 60 * ((g - b) / dist)
			elif (tmax == g):
				th = 60 * ((b - r) / dist)
			elif (tmax == b):
				th = 60 * ((r - g) / dist)

			if(th < 0):
				th += 360

			if(tmax == 0):
				ts = 0
			else:
				ts = dist / tmax
			
			h[i,j] = th / 360
			s[i,j] = ts
			v[i,j] = tmax

	return h, s, v

def rgb_to_hsi(img):
	shape = img.shape[:2]
	h = np.zeros(shape)
	s = np.zeros(shape)
	vi = np.zeros(shape)

	tmp = img/255
	for i in range(0, img.shape[0]):
		for j in range(0, img.shape[1]):
			px = tmp[i,j]
			b, g, r = px

			tmin = px.min()
			tmax = px.max()
			dist = tmax - tmin

			if(tmax == tmin):
				th = 0
			elif (tmax == r):
				th = 60 * ((g - b) / dist)
			elif (tmax == g):
				th = 60 * ((b - r) / dist)
			elif (tmax == b):
				th = 60 * ((r - g) / dist)

			if(th < 0):
				th += 360

			if(tmax == 0 or tmax == 1):
				ts = 0
			else:
				tp = px.sum()
				if(tp != 0):
					ts = 1 - ((3 * tmin) / tp)
				else:
					ts = 1

			h[i,j] = th / 360
			s[i,j] = ts
			vi[i,j] = px.mean()

	return h, s, vi


def rgb_to_hsit(img, eps = 0.001):
	img = img/255
	shape = img.shape[:2]

	h = np.zeros(shape)
	s = np.zeros(shape)
	vi = np.zeros(shape)

	for i in range(0, img.shape[0]):
		for j in range(0, img.shape[1]):
			px = img[i,j]
			tmin = px.min()
			b, g, r = px

			th = 0.5 * ((r-g) + (r-b)) / sqrt( ((r-g)**2) + ((r-b)*(g-b)))
			th = acos(th)

			if(b <= g):
				h[i,j] = th
			else:
				h[i,j] = (2*np.pi) - th
			
			s[i,j] = 1 - ((3 * tmin) / (px.sum() + eps))
			vi[i,j] = px.mean()

	return h, s, vi


def rgb_to_yuv(img):
	img = img/255
	shape = img.shape[:2]

	y = np.zeros(shape)
	u = np.zeros(shape)
	v = np.zeros(shape)

	vals = np.array([ [0.299, 0.587, 0.144],
        			  [-0.147, -0.289, 0.436],
        			  [0.615, -0.5151, -0.1] ])


	for i in range(0, img.shape[0]):
		for j in range(0, img.shape[1]):
			yuv = np.dot(vals, img[i,j][::-1])
			y[i,j] = yuv[0]# * 255
			u[i,j] = yuv[1]# * 255
			v[i,j] = yuv[2]# * 255

	return y, u, v

def rgb_to_yiq(img):
	img = img/255
	shape = img.shape[:2]

	y = np.zeros(shape)
	ti = np.zeros(shape)
	q = np.zeros(shape)

	vals = np.array([ [0.299, 0.587, 0.144],
					  [0.596, -0.275, -0.321],
					  [0.212, -0.523, 0.311] ])


	for i in range(0, img.shape[0]):
		for j in range(0, img.shape[1]):
			yiq = np.dot(vals, img[i,j][::-1])
			y[i,j] = yiq[0]# * 255
			ti[i,j] = yiq[1]# * 255
			q[i,j] = yiq[2]# * 255

	return y, ti, q

def rgb_to_ycbcr(img):
	img = img/255
	shape = img.shape[:2]

	y = np.zeros(shape, dtype='uint8')
	cb = np.zeros(shape, dtype='uint8')
	cr = np.zeros(shape, dtype='uint8')

	vals = np.array([ [65.481, 128.553, 24.966],
					  [-37.797, -74.203, 112],
					  [112, -93.786, -18.214] ])

	for i in range(0, img.shape[0]):
		for j in range(0, img.shape[1]):
			ycbcr = np.dot(vals, img[i,j][::-1])
			y[i,j] = ycbcr[0] + 16
			cb[i,j] = ycbcr[1] + 128
			cr[i,j] = ycbcr[2] + 128

	return y, cb, cr