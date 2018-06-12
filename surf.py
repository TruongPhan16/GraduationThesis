import numpy as np
import cv2
import os
from os import listdir
from os.path import isfile, join

surf = cv2.xfeatures2d.SURF_create()
surf.setHessianThreshold(400)
def getKpFromImages(path,folder1):
  fileName = []
  files = [ f for f in listdir(path) if isfile(join(path,f)) ]
  images = np.empty(len(files), dtype=object)
  if not os.path.exists(folder1):
    os.makedirs(folder1)
  for n in range(0, len(files)):
    images[n] = cv2.imread( join(path,files[n]))
    gray = cv2.cvtColor(images[n],cv2.COLOR_BGR2GRAY)
    kp, des = surf.detectAndCompute(gray,None)
    fileName.append(os.path.splitext(os.path.basename(files[n]))[0])
    np.savetxt(folder1 + '/' + str(fileName[n]) + '.txt' ,des,delimiter=',')
  return fileName