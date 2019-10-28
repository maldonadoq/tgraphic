import numpy as np
import cv2 as cv

def binarization(src):
    ret, img = cv.threshold(src, 127, 255, cv.THRESH_BINARY)
    return img/255

def erosion_op(w, s):
    for i in range(s.shape[0]):
        for j in range(s.shape[1]):
            if((s[i,j] == 1) and (w[i,j] == 0)):
                return False
    return True

def erosion(src, s):
    img = np.zeros(src.shape)
    step = s.shape[0] // 2
    for i in range(step, src.shape[0] - step):
        rt0 = i - step
        rt1 = i + step + 1
        for j in range(step, src.shape[1] - step):
            ct0 = j - step
            ct1 = j + step + 1
            w = src[rt0:rt1, ct0:ct1]            
            if(erosion_op(w,s)):
                img[i,j] = 1
    return img

def dilatation(src, s):
    img = np.zeros(src.shape)
    step = s.shape[0] // 2

    for i in range(step, src.shape[0] - step):
        rt0 = i - step
        for j in range(step, src.shape[1] - step):
            ct0 = j - step
            if(src[i,j] == 1):
                for x in range(s.shape[0]):
                    for y in range(s.shape[1]):
                        if(s[x,y] == 1):
                            img[rt0 + x, ct0 + y] = 1

    return img

def opening(src, s):
    e = erosion(src,s)
    d = dilatation(e, s)

    return d

def closing(src, s):
    d = dilatation(src,s)
    e = erosion(d, s)

    return e

def complement(src):
    img = np.ones(src.shape)
    for i in range(src.shape[0]):
        for j in range(src.shape[1]):
            if(src[i,j] == 1):
                img[i,j] = 0
    return img

def tor(src1, src2):
    img = np.zeros(src1.shape)
    for i in range(src1.shape[0]):
        for j in range(src1.shape[1]):
            if(src1[i,j] or src2[i,j]):
                img[i,j] = 1

    return img

def hit_miss(src, s1, s2):
    e1 = erosion(src,s1)
    C = complement(src)
    e2 = erosion(C,s2)
    h = tor(e1,e2)
    
    return h