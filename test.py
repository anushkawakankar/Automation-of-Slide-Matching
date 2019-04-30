import cv2
import os
import sys
# from skimage.measure import compare_ssim
from SSIM_PIL import compare_ssim
from PIL import Image

def read_img(folder):
    frames = []
    names = []
    for filename in os.listdir(folder):
        # img = cv2.imread(os.path.join(folder,filename))
        # img = mpimg.imread(os.path.join(folder,filename))
        img = Image.open(os.path.join(folder,filename))
        if img is not None:
            frames.append(img)
            names.append(filename)
    return frames,names

def show_img(arr,names):
    count = 0
    l = len(arr)
    for i in range(l):
        # cv2.imshow(names[i],arr[i])
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        # plt.imshow(names[i])
        arr[i].show()

def print_diff(frames,slides):
    f = len(frames)
    s = len(slides)
    for i in range(f):
        # frames[i] = cv2.cvtColor(frames[i], cv2.COLOR_BGR2GRAY)
        frames[i] = frames[i].convert("L")
    for i in range(s):
        # slides[i] = cv2.cvtColor(slides[i], cv2.COLOR_BGR2GRAY)
        slides[i] = slides[i].convert("L")
    #
    for i in range(f):
        # print(i)
        allScores = []
        # count = 0
        for j in range(s):
            # (score,diff) = compare_ssim(frames[i], slides[j], full=True)
            # score = ssim(frames[i], slides[j])
            score = compare_ssim(frames[i],slides[j])
            allScores.append(score)
            # count = count + 1
        orig = allScores.index(max(allScores))
        print(framename[i]," ",slidename[orig])
        # print(orig+1)



frames = []
slides = []
framename = []
slidename = []
frames,framename = read_img(sys.argv[2])
slides,slidename = read_img(sys.argv[1])

print_diff(frames,slides)
# show_img(frames,framename)
# show_img(slides,slidename)
