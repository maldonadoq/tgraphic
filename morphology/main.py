import numpy as np
import cv2 as cv

import sys

sys.path.append('src/')
from structure import *

if __name__ == "__main__":
	img = cv.imread('../images/input/cube.png')

	#cv.imshow('Cube', img)

	dim = 3
	if(len(sys.argv) == 2):
		dim = int(sys.argv[1])

	s = structure(2, dim)

	print(s)

	#cv.waitKey()
	#cv.destroyAllWindows()