import numpy as np

# Lineal and Estadistic Filters
def lfilter(img_in, wsize, op):
    rows = img_in.shape[0]
    cols = img_in.shape[1]

    img_out = np.zeros(img_in.shape, img_in.dtype)
    step = wsize//2

    for i in range(step, rows - step):
        rt0 = i - step
        rt1 = i + step + 1
        for j in range(step, cols - step):
            ct0 = j - step
            ct1 = j + step + 1
            window = img_in[rt0:rt1, ct0:ct1]
            img_out[i,j] = op(window)

    return img_out

def mnormalize(img_in):
    img_out = np.zeros(img_in.shape, dtype="uint8")
    tmin = img_in.min()
    tmax = img_in.max()
    nmax = abs(tmax - tmin)

    for i in range(img_out.shape[0]):
        for j in range(img_out.shape[1]):
            nv = ((img_in[i,j] - tmin) * 255)/nmax
            img_out[i,j] = nv

    return img_out

# Filters with only one mask (Laplace, Gauss)
def mfilter(img_in, hfilter):
    img_out = np.zeros(img_in.shape, int)
    rows = img_in.shape[0]
    cols = img_in.shape[1]

    if(hfilter.shape[0] != hfilter.shape[1]):
        print("The shape would be a square!")
        return img_out
    
    wsize = hfilter.shape[0]
    step = wsize//2

    for i in range(step, rows - step):
        rt0 = i - step
        rt1 = i + step + 1
        for j in range(step, cols - step):
            ct0 = j - step
            ct1 = j + step + 1
            window = img_in[rt0:rt1, ct0:ct1]
            #nv = (window * hfilter).sum()
            nv = abs((window * hfilter).sum())
            img_out[i,j] = nv
            
    return mnormalize(img_out)

# Filters with two mask (Robert, Sobel, Prewitt)
def nfilter(img_in, xfilter, yfilter):
    img_out = np.zeros(img_in.shape, int)
    rows = img_in.shape[0]
    cols = img_in.shape[1]

    if((xfilter.shape != yfilter.shape) and (xfilter.shape[0] != xfilter.shape[1])):
        print("both matrix would be same shape and shape would be a square!")
        return img_out
    
    wsize = xfilter.shape[0]
    step = wsize//2

    for i in range(step, rows - step):
        rt0 = i - step
        rt1 = i + step + 1
        for j in range(step, cols - step):
            ct0 = j - step
            ct1 = j + step + 1
            window = img_in[rt0:rt1, ct0:ct1]
            #hx = (window*xfilter).sum()
            #hy = (window*yfilter).sum()
            hx = abs((window*xfilter).sum())
            hy = abs((window*yfilter).sum())

            img_out[i,j] = hx + hy

    return mnormalize(img_out)