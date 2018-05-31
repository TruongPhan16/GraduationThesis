import cv2
import numpy as np
import os
from os import listdir
from os.path import isfile, join

def getKpForTrainingData(path,folder):
  fileName = []
  sift = cv2.xfeatures2d.SIFT_create()
  files = [ f for f in listdir(path) if isfile(join(path,f)) ]
  images = np.empty(len(files), dtype=object)
  if not os.path.exists(folder):
    os.makedirs(folder)
  for n in range(0, len(files)):
    images[n] = cv2.imread( join(path,files[n]))
    gray = cv2.cvtColor(images[n],cv2.COLOR_BGR2GRAY)
    kp = sift.detect(images[n],None)
    kp,des = sift.compute(gray,kp)
    fileName.append(os.path.splitext(os.path.basename(files[n]))[0])
    np.savetxt(folder + '/' + str(fileName[n]) + '.txt' ,des,delimiter=',')
  return fileName
  
def getKpForTestData(img,file):
  sift = cv2.xfeatures2d.SIFT_create()
  image = cv2.imread(img + '.jpg')
  gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
  kp = sift.detect(image,None)
  kp,des = sift.compute(gray,kp)
  np.savetxt(file + '.txt' ,des,delimiter=',')
