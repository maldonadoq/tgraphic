from math import (cos, sin, radians, floor, ceil)
import numpy as np
import cv2 as cv

def mtranslation(img_in, tx, ty):
	shape = img_in.shape[0] + abs(ty), img_in.shape[1] + abs(tx)
	img_out = np.zeros(shape, img_in.dtype)

	for i in range(0, img_in.shape[0]):
		for j in range(0, img_in.shape[1]):
			if tx < 0 and ty < 0:					# move to left and up
				img_out[i, j] = img_in[i,j]
			elif tx < 0:							# move to left and down
				img_out[i+ty, j] = img_in[i,j]
			elif ty < 0:							# move to right and up
				img_out[i, j+tx] = img_in[i,j]
			else:
				img_out[i+ty, j+tx] = img_in[i,j]	# move to right and down
	return img_out

def mscale(img_in, sx, sy):
	shape = (floor(img_in.shape[0]*sy), floor(img_in.shape[1]*sx))
	img_out = np.empty(shape, img_in.dtype)

	for i in range(shape[0]):
		for j in range(shape[1]):
			img_out[i, j] = img_in[floor(i // sy), floor(j // sx)]

	return img_out

def mrotate_point(point, angle, center):
	x, y = point
	cx, cy = center
	tcos = cos(angle)
	tsin = sin(angle)

	x -= cx
	y -= cy

	tx = (x*tcos) + (y*tsin)
	ty = -(x*tsin) + (y*tcos)

	return round(tx + cx), round(ty + cy)

def mrotate(img_in, angle, center = None):
	img_out = np.zeros(img_in.shape, img_in.dtype)
	rows = img_in.shape[0]
	cols = img_in.shape[1]

	shape = (rows*2, cols*2)
	img_out = np.zeros(shape, img_in.dtype)

	if(center is None):
		center = (rows//2, cols//2)

	angle = radians(angle)
	for i in range(rows):
		for j in range(cols):
			x, y = mrotate_point((j, i), angle, center)

			x += shape[1]//4
			y += shape[0]//4 

			if 0 <= x < shape[1] and 0 <= y < shape[0]:
				img_out[y,x] = img_in[i,j]

	return img_out

if __name__ == "__main__":
    img = cv.imread('../images/input/lena.jpg', 0)

    ttrans  = mtranslation(img, 50, -50)
    tscale  = mscale(img, 2, 2)
    trotate = mrotate(img, 45)

    cv.imwrite('../images/output/translation.jpg', ttrans)
    cv.imwrite('../images/output/scale.jpg', tscale)
    cv.imwrite('../images/output/rotate.jpg', trotate)

    """cv.imshow('Translation', ttrans)
    cv.imshow('Scale', tscale)
    cv.imshow('Rotate', trotate)

    cv.waitKey()
    cv.destroyAllWindows()"""