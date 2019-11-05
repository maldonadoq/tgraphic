from math import ceil, sqrt
import numpy as np
from random import randint

# Wikipedia
def histogram(src):
    hist = np.zeros(256, dtype=int)

    for i in range(src.shape[0]):
        for j in range(src.shape[1]):
            hist[src[i,j]] = hist[src[i,j]] + 1
    
    return hist

def otsu(src, hist):
    fl = src.flatten()
    n = fl.size
    norm = hist / n
    max_delta = 0

    for t in range(255):
        mu0 = 0
        mu1 = 0

        ome0 = np.sum(norm[0:t+1])
        ome1 = 1 - ome0

        for i in range(t+1):
            mu0 = mu0 + i * norm[i]

        if(ome0 != 0):
            mu0 = mu0 / ome0

        for i in range(t+1,256):
            mu1 = mu1 + i * norm[i]

        if(ome1 != 0):
            mu1 = mu1 / ome1
        
        delta = ome0 * ome1 * pow(mu0 - mu1,2)

        if(max_delta < delta):
            max_delta = delta
            th = t

    return th

def threshold(src, t):
    img = np.zeros(src.shape, dtype='uint8')

    for i in range(src.shape[0]):
        for j in range(src.shape[1]):
            if(src[i,j] > t):
                img[i,j] = 255                

    return img

# Professor
def adaptative_otsu(src, n):
    img = np.zeros(src.shape)
    rows, cols = src.shape[:2]

    nr = ceil(rows / n)
    nc = ceil(cols / n)
    box = []

    for i in range(n):
        for j in range(n):
            box.append([i*nr, j*nc, min((i+1)*nr, rows), min((j+1)*nc, cols)])

    for bx in box:
        bb = src[bx[0]:bx[2], bx[1]:bx[3]]

        hist = histogram(bb)
        t = otsu(bb, hist)
        seg = threshold(bb, t)
        img[bx[0]:bx[2], bx[1]:bx[3]] = seg

    return img


# Paper https://people.ece.cornell.edu/acharya/papers/mlt_thr_img.pdf
def sujov(src, a, b):
    if(a > b):
        return (-1,-1)

    t1 = (src >= a)
    t2 = (src <= b)

    X = t1 * t2
    Y = src * X

    s = X.sum()
    m = Y.sum() / s

    return (m,s)

def multi_threshold(src, h, a = 0, b = 255, n = 6, k = 0.7):
    T = []
    for i in range(int(h/2 - 1)):
        t1 = (src >= a)
        t2 = (src <= b)

        X = t1 * t2
        Y = src * X
        mu = Y.sum() / X.sum()

        Z = Y - mu
        Z = Z * X
        W = Z * Z
        sigma = sqrt(W.sum() / X.sum())

        T1 = mu - (k*sigma)
        T2 = mu + (k*sigma)

        x, y = sujov(src, a, T1)
        w, z = sujov(src, T2, b)

        T.append(x)
        T.append(w)

        a = T1 + 1
        b = T2 - 1

        k = k * (i + 1)

    T1 = mu
    T2 = mu + 1
    x, y = sujov(src, a, T1)
    w, z = sujov(src, T2, b)

    T.append(x)
    T.append(w)
    T.sort()

    return T

# Color
def random_color(n):
    color = []

    for i in range(n):
        color.append([randint(0, 255), randint(0, 255), randint(0, 255)])
    
    return color

def threshold_range(T):
    r = []
    s = len(T) - 1
    
    r.append([0, int(T[0])])
    for i in range(s):
        r.append([int(T[i]),int(T[i+1])])
    r.append([int(T[s]), 256])

    return r

def inside(v, T):
    for i in range(len(T)):
        if((v >= T[i][0]) and (v < T[i][1])):
            return i

def segmentation(src, T):
    colors = random_color(len(T) + 1)
    trange = threshold_range(T)
    rows, cols = src.shape[:2]

    img = np.zeros((rows,cols,3), dtype='uint8')
    for i in range(src.shape[0]):
        for j in range(src.shape[1]):
            idx = inside(src[i,j], trange)
            #print(idx, end=' ')
            img[i,j] = colors[idx]

    return img