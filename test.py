import cv2
import os
# from skimage.measure import structural_similarity as ssim
from skimage.measure import compare_ssim
# import imutils

def read_img(folder):
    frames = []
    names = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            frames.append(img)
            names.append(filename)
    return frames,names

def show_img(arr,names):
    count = 0
    l = len(arr)
    for i in range(l):
        cv2.imshow(names[i],arr[i])
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def print_diff(frames,slides):
    f = len(frames)
    s = len(slides)
    for i in range(f):
        frames[i] = cv2.cvtColor(frames[i], cv2.COLOR_BGR2GRAY)
    for i in range(s):
        slides[i] = cv2.cvtColor(slides[i], cv2.COLOR_BGR2GRAY)

    for i in range(f):
        # print(i)
        allScores = []
        # count = 0
        for j in range(s):
            (score,diff) = compare_ssim(frames[i], slides[j], full=True)
            # score = ssim(frames[i], slides[j])
            allScores.append(score)
            # count = count + 1
        orig = allScores.index(max(allScores))
        print(framename[i]," ",slidename[orig])
        # print(orig+1)



frames = []
slides = []
framename = []
slidename = []
frames,framename = read_img("frames")
slides,slidename = read_img("slides")

print_diff(frames,slides)
# show_img(frames,framename)
# show_img(slides,slidename)

# cv2.imshow("", frames[4])
# print(framename[4])
# cv2.waitKey(0)
# cv2.destroyAllWindows()
