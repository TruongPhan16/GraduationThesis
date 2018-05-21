import cv2
import numpy as np
import os
from os import listdir
from os.path import isfile, join

sift = cv2.xfeatures2d.SIFT_create()
path = 'training'
files = [ f for f in listdir(path) if isfile(join(path,f)) ]
images = np.empty(len(files), dtype=object)
dirFolder = 'sift'
os.mkdir(dirFolder)
fileName = []
for n in range(0, len(files)):
  images[n] = cv2.imread( join(path,files[n]))
  gray = cv2.cvtColor(images[n],cv2.COLOR_BGR2GRAY)
  kp = sift.detect(images[n],None)
  kp,des = sift.compute(gray,kp)
  fileName.append(os.path.splitext(os.path.basename(files[n]))[0])
  np.savetxt(dirFolder + '/' + str(fileName[n]) + '.txt' ,des,delimiter=',')
