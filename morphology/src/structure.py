import numpy as np
from math import sqrt, pow

def square(dim):
    strt = np.ones((dim,dim))
    return strt

def circle(dim):
    strt = np.zeros((dim,dim))
    c = (dim-1)/2

    for i in range(dim):
        for j in range(dim):
            dist = sqrt(pow(i-c,2) + pow(j-c,2))
            if(dist <= c):
                strt[i,j] = 1

    return strt

def cross(dim):

    if(dim == 3):
        return np.array([[0,1,0],[1,1,1],[0,1,0]])
    if(dim == 4):
        return np.array([[0,1,1,0],[1,1,1,1],[1,1,1,1],[0,1,1,0]])

    strt = np.zeros((dim,dim))
    s = dim//4
    t = dim - s
    c = t//2

    if(t%2 != 0):
        s+=1

    strt[c:c+s,0:dim] = 1   # hor
    strt[0:dim,c:c+s] = 1   # ver

    return strt

def diamond(dim):
    strt = np.ones((dim,dim))
    s = dim//4
    c = (dim-s)//2

    return strt

def structure(id = 0, dim = 3):
    if(id == 0):
        s = square(dim)
    elif(id == 1):
        s = circle(dim)
    elif(id == 2):
        s = cross(dim)

    return s