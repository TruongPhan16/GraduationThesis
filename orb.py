import numpy as np
import cv2
import os
from os import listdir
from os.path import isfile, join


orb = cv2.ORB_create()
path = 'training'
files = [ f for f in listdir(path) if isfile(join(path,f)) ]
images = np.empty(len(files), dtype=object)
dirFolder = 'orb'
os.mkdir(dirFolder)

for n in range(0, len(files)):
  images[n] = cv2.imread( join(path,files[n]))
  kp = orb.detect(images[n],None)
  kp, des = orb.compute(images[n], kp)
  with open('C:\\Python27\\orb\\'+str(n)+'.csv', 'wb') as f:
     writer = csv.writer(f)
     for(i in des):
       writer.writerow(i)
