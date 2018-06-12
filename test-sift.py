import cv2
import numpy as np
import math
import glob
import sift as sift
from collections import Counter
import time

trainingData = []
testData = []
k = 5
# fileNameTraining = sift.getKpFromImages('training','sift')
# fileNameTest = sift.getKpFromImages('test-images','test-data')
#t = 200 is best, 
start = time.time()
sift.getKpFromImages('t-1','t-2')
end = time.time()
print(end - start)
def euclidean(vector1, vector2):
    dist = [(a - b)**2 for a, b in zip(np.array(vector1), np.array(vector2))]
    dist = math.sqrt(sum(dist))
    return dist

def findDistance(v1, v2, t):
    count = 0
    for i in v1:
        for j in v2:
            dist = euclidean(i,j)
            if (dist < t):
                count += 1
    return float(count) / float(len(v1) * len(v2))

def readTestData(path) :
    path = path + '/*.txt'
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            data = f.readline().strip().splitlines()
            dataArrParse = []
            for value in data:
                arr = value.split(',')
                arrayParse = []
                for j in arr:
                    dataParse = float(j)
                    arrayParse.append(dataParse)
                dataArrParse.append(arrayParse)
            testData.append(dataArrParse)
# readTestData('test-data')

def readTrainingData(path):
    path = path + '/*.txt'
    files = glob.glob(path)
    arrResult = []
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
    for tr in testData:
        tmp = []
        for te in trainingData:
            result = findDistance(tr,te,200)
            tmp.append(result)
        tmp = np.array(tmp).argsort()[::-1][:k]
        arrResult.append(tmp)
    return arrResult

def calculateEfficiency():
    filledImages = readTrainingData('sift')
    total = 0
    for (key, value) in enumerate(filledImages):
        imageNameTest = fileNameTest[key]
        arr = []
        for index in value:
            image = fileNameTraining[index]
            arr.append(image)
            imageNameTrain = Counter(arr).most_common(1)[0][0]
        if imageNameTest[:4] == imageNameTrain[:4]:
            total += 1
    efficiency = float(total) / float(len(fileNameTest))
    print efficiency
# calculateEfficiency()

