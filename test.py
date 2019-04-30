import os
import sys
import numpy
from PIL import Image
from scipy import signal
from scipy import ndimage


def gaussf(size,sigma):
    shape = (size,size)
    m,n = [(ss-1.)/2. for ss in shape]
    y,x = numpy.ogrid[-m:m+1,-n:n+1]
    h = numpy.exp( -(x*x + y*y) / (2.*sigma*sigma) )
    h[ h < numpy.finfo(h.dtype).eps*h.max() ] = 0
    sumh = h.sum()
    if sumh != 0:
        h /= sumh
    return h

def my_ssim(img1, img2):
    img1 = img1.astype(numpy.float64)
    img2 = img2.astype(numpy.float64)
    size = 11
    sigma = 1.5
    # window = gauss.fspecial_gauss(size, sigma)
    window = gaussf(size,sigma)
    K1 = 0.01
    K2 = 0.03
    L = 255
    C1 = (K1*L)**2
    C2 = (K2*L)**2
    # print(window.shape, img1.shape)
    mu1 = signal.fftconvolve(window, img1, mode='valid')
    mu2 = signal.fftconvolve(window, img2, mode='valid')
    mu1_sq = mu1*mu1
    mu2_sq = mu2*mu2
    mu1_mu2 = mu1*mu2
    sigma1_sq = signal.fftconvolve(window, img1*img1, mode='valid') - mu1_sq
    sigma2_sq = signal.fftconvolve(window, img2*img2, mode='valid') - mu2_sq
    sigma12 = signal.fftconvolve(window, img1*img2, mode='valid') - mu1_mu2

    return ((2*mu1_mu2 + C1)*(2*sigma12 + C2))/((mu1_sq + mu2_sq + C1)*(sigma1_sq + sigma2_sq + C2))



def read_img(folder):
    frames = []
    names = []
    for filename in os.listdir(folder):
        img = Image.open(os.path.join(folder,filename))
        img = img.convert("L")
        img = numpy.asarray(img)
        # img = Image.open(os.path.join(folder,filename))
        if img is not None:
            frames.append(img)
            names.append(filename)
    return frames,names

def show_img(arr,names):
    count = 0
    l = len(arr)
    for i in range(l):
        arr[i].show()

def print_diff(frames,slides):
    f = len(frames)
    s = len(slides)
    for i in range(f):
        allScores = []
        for j in range(s):
            score = my_ssim(frames[i],slides[j])
            allScores.append(score.mean())
        orig = allScores.index(max(allScores))
        print(framename[i]," ",slidename[orig])



frames = []
slides = []
framename = []
slidename = []
frames,framename = read_img(sys.argv[2])
slides,slidename = read_img(sys.argv[1])

print_diff(frames,slides)
# show_img(slides,slidename)
