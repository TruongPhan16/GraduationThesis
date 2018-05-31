import numpy as np
import cv2
import os
from os import listdir
from os.path import isfile, join

surf = cv2.xfeatures2d.SURF_create()
path = 'training'
files = [ f for f in listdir(path) if isfile(join(path,f)) ]
images = np.empty(len(files), dtype=object)
dirFolder = 'surf'
os.mkdir(dirFolder)

for n in range(0, len(files)):
  images[n] = cv2.imread( join(path,files[n]))
  kp, des = surf.detectAndCompute(images[n],None)
  with open('C:\\Python27\\surf\\'+str(n)+'.csv', 'wb') as f:
     writer = csv.writer(f)
     writer.writerow(des)