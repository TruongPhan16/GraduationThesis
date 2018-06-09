import numpy as np
import cv2
import os
from os import listdir
from os.path import isfile, join

def getKpFromImages(path,folder):
  orb = cv2.ORB_create()
  fileName = []
  files = [ f for f in listdir(path) if isfile(join(path,f)) ]
  images = np.empty(len(files), dtype=object)
  if not os.path.exists(folder):
    os.makedirs(folder)
  for n in range(0, len(files)):
    images[n] = cv2.imread( join(path,files[n]))
    kp = orb.detect(images[n],None)
    kp, des = orb.compute(images[n], kp)
    fileName.append(os.path.splitext(os.path.basename(files[n]))[0])
    np.savetxt(folder + '/' + str(fileName[n]) + '.txt' ,des,delimiter=',')
  return fileName

