import cv2
import numpy as np
import math
import glob
import surf as surf

trainingData = []
testData = []
fileList = surf.getKpFromImages('training','surf')

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
readTestData('surf')

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
        tmp = np.array(tmp).argsort()[::-1][:5]
        arrResult.append(tmp)
    return arrResult

def calculateEfficiency():
    filledImages = readTrainingData('surf')
    total = 0
    for (key, value) in enumerate(filledImages):
        imageNameTest = fileList[key]
        countSameName = 0
        for index in value:
            imageNameTrain = fileList[index]
            if imageNameTest[:4] == imageNameTrain[:4]:
                countSameName += 1
        total += countSameName/5
    efficiency = total / len(fileList)
    print efficiency
calculateEfficiency()
