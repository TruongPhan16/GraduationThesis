import numpy as np
import cv2
import os
from os import listdir
from os.path import isfile, join

surf = cv2.xfeatures2d.SURF_create()
def getKpFromImages(path,folder1):
  fileName = []
  files = [ f for f in listdir(path) if isfile(join(path,f)) ]
  images = np.empty(len(files), dtype=object)
  if not os.path.exists(folder1):
    os.makedirs(folder1)
  for n in range(0, len(files)):
    images[n] = cv2.imread( join(path,files[n]))
    kp, des = surf.detectAndCompute(images[n],None)
    fileName.append(os.path.splitext(os.path.basename(files[n]))[0])
    np.savetxt(folder1 + '/' + str(fileName[n]) + '.txt' ,des,delimiter=',')
    # np.savetxt(folder2 + '/' + str(fileName[n]) + '.txt' ,des,delimiter=',')
  return fileName