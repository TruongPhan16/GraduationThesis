import numpy as np
import cv2
import os
from os import listdir
from os.path import isfile, join

surf = cv2.xfeatures2d.SURF_create()
def getKpForTrainingData(path,folder):
  fileName = []
  files = [ f for f in listdir(path) if isfile(join(path,f)) ]
  images = np.empty(len(files), dtype=object)
  if not os.path.exists(folder):
    os.makedirs(folder)
  for n in range(0, len(files)):
    images[n] = cv2.imread( join(path,files[n]))
    kp, des = surf.detectAndCompute(images[n],None)
    fileName.append(os.path.splitext(os.path.basename(files[n]))[0])
    np.savetxt(folder + '/' + str(fileName[n]) + '.txt' ,des,delimiter=',')
  return fileName

def getKpForTestData(img,file):
  image = cv2.imread(img + '.jpg')
  kp,des = surf.detectAndCompute(image,None)
  np.savetxt(file + '.txt' ,des,delimiter=',')