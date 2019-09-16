import numpy as np
from random import randint

mat = np.empty((4,4), int)

for i in range(mat.shape[0]):
    for j in range(mat.shape[1]):
        mat[i,j] = randint(0, 9)

#print(mat)

#wind = mat[1:2, 1:6]
#wind = mat[0:4, 0:2]
#print("\n", wind)

def mfilter(img_in, wsize):
    rows = img_in.shape[0]
    cols = img_in.shape[1]

    img_out = np.empty(img_in.shape, img_in.dtype)
    step = wsize//2

    tmp = 0
    for i in range(step, rows - step):
        rt0 = i - step
        rt1 = i + step + 1
        for j in range(step, cols - step):
            ct0 = j - step
            ct1 = j + step + 1
            window = img_in[rt0:rt1, ct0:ct1]
            #img_out[i, j] = op(window)
            print("\n", tmp, "\n", window)
            tmp += 1
    #return img_out

#mfilter(mat, 3)


a = np.array([[1,2], [3,4]])
b = np.array([[4,3], [2,1]])

d1 = np.dot(a,b)
d2 = a*b

print(d1)
print(d2)