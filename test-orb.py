import cv2
import numpy as np
import math
import glob
import orb as orb
from collections import Counter

trainingData = [] #135 anh
testData = [] #16 anh
k = 5
fileNameTraining = orb.getKpFromImages('training','orb')
fileNameTest = orb.getKpFromImages('test-images', 'test-data')
#t = 300 is best
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
            if (dist < t):
                count +=1
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
readTestData('test-data')

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
            result = findDistance(tr,te,300)
            tmp.append(result)
        tmp = np.array(tmp).argsort()[::-1][:k]
        arrResult.append(tmp)
    return arrResult

def calculateEfficiency():
    filledImages = readTrainingData('orb')
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
    print total
    print efficiency
calculateEfficiency()
