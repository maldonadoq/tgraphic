import numpy as np

def histogram(src):
    hist = np.zeros(256, dtype=int)

    for i in range(src.shape[0]):
        for j in range(src.shape[1]):
            hist[src[i,j]] = hist[src[i,j]] + 1
    
    return hist

def otsu_threshold(src, hist):
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
            threshold = t

    return threshold

def segmentation(src, t):
    img = np.zeros(src.shape, dtype='uint8')

    for i in range(src.shape[0]):
        for j in range(src.shape[1]):
            if(src[i,j] > t):
                img[i,j] = 255                

    return img