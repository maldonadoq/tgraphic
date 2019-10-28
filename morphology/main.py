import numpy as np
import cv2 as cv

import sys

sys.path.append('src/')
from structure import *
from operation import *

if __name__ == "__main__":
	img = cv.imread('../images/input/sample1.png', 0)
	#img = binarization(img)
	img = img/255

	t = 0
	r = 'e'

	if(len(sys.argv) == 2):
		t = int(sys.argv[1])
	elif(len(sys.argv) == 3):
		r = sys.argv[1]
		t = int(sys.argv[2])
	elif(len(sys.argv) == 4):
		r = sys.argv[1]
		t = int(sys.argv[2])
		t2 = int(sys.argv[3])

	s = structure_static(t)
	if(r == 'd'):
		print('Dilatation')
		p = dilatation(img, s)
	elif(r == 'o'):
		print('Opening')
		p = opening(img, s)
	elif(r == 'c'):
		print('Closing')
		p = closing(img, s)
	elif(r == 'h'):
		print('Hit or Miss')
		s1 = structure_static(t2)
		p = hit_miss(img, s, s1)
	else:
		print('Erosion')
		p = erosion(img, s)

	src = np.concatenate((img, p), axis=1)
	cv.imshow('Normal - [X]', src)

	cv.waitKey()
	cv.destroyAllWindows()