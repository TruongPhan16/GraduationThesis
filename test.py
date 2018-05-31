import cv2
import numpy as np
import math
import glob
import sift as sift

trainingData = []
testData = []

fileList = sift.getKpForTrainingData('training','sift')
sift.getKpForTestData('test-sift','test-sift')

def euclidean(vector1, vector2):
    dist = [(a - b)**2 for a, b in zip(np.array(vector1), np.array(vector2))]
    dist = math.sqrt(sum(dist))
    return dist

def findDistance(v1, v2, t):
    count = 0
    for i in v1:
        distance = []
        for j in v2:
            dist = euclidean(i,j)
            # distance.append(dist)
        # minDistance = min(float(s) for s in distance)
            if (dist < t):
                count +=1
    return float(count) / float(len(v1) * len(v2))

def readTestData(name) :
    name = name + '.txt'
    with open(name) as f:
        for line in f:
            innerList = [float(elt.strip()) for elt in line.split(',')]
            testData.append(innerList)
readTestData('test-sift')

def readTrainingData(p):
    path = p + '/*.txt'
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            data = f.read().strip().splitlines()
            dataArrParse = []
            for value in data:
                arr = value.split(',')
                arrayParse = []
                for j in arr:
                    dataParse = float(j)
                    arrayParse.append(dataParse)
                dataArrParse.append(arrayParse)
            trainingData.append(dataArrParse)
    arrResult = []
    for img in trainingData:
        result = findDistance(testData,img,200)
        arrResult.append(result)
    maxIndices = np.array(arrResult).argsort()[::-1][:5]
    return maxIndices

filledImages = readTrainingData('sift')
for index in filledImages:
    image = cv2.imread('training/' + fileList[index] + '.jpg') 
    cv2.imshow('image',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
