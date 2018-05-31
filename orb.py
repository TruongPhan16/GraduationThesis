import numpy as np
import cv2
import os
from os import listdir
from os.path import isfile, join

orb = cv2.ORB_create()
def getKpForTrainingData(path,folder):
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

def getKpForTestData(img,file):
  image = cv2.imread(img + '.jpg')
  kp = orb.detect(image,None)
  kp,des = orb.compute(image,kp)
  np.savetxt(file + '.txt' ,des,delimiter=',')

