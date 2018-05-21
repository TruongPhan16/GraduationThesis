import cv2
import numpy as np
import math
import glob

trainingData = []
testData = []

# def getKpForTestData(img,file):
#     sift = cv2.xfeatures2d.SIFT_create()
#     image = cv2.imread(img + '.jpg',1)
#     gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#     kp = sift.detect(image,None)
#     kp,des = sift.compute(gray,kp)
#     np.savetxt(file + '.txt' ,des,delimiter=',')
# getKpForTestData('test2','test')

def euclidean(vector1, vector2):
    dist = [(a - b)**2 for a, b in zip(np.array(vector1), np.array(vector2))]
    dist = math.sqrt(sum(dist))
    return dist

def readTestData(name) :
    name = name + '.txt'
    with open(name) as f:
        for line in f:
            innerList = [float(elt.strip()) for elt in line.split(',')]
            testData.append(innerList)
readTestData('test')

def readTrainingData(p):
    path = p + '/*.txt'
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            data = f.read().strip().replace('\n', ',').split(',')
            arrayParse = []
            for value in data:
                dataParse = float(value)
                arrayParse.append(dataParse)
    trainingData.append(arrayParse)
readTrainingData('sift')
print trainingData[0][0]
def findDistance(v1, v2, t):
    distance = []
    for i in v1:
        for j in v2:
            dist = euclidean(i,j)
            distance.append(dist)
    # minDistance = min(float(s) for s in distance)
    return minn
# print(findDistance(testData, trainingData,400))