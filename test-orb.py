import cv2
import numpy as np
import math
import glob
import sift as sift
import orb as orb
import surf as surf

trainingData = []
testData = []

fileList = orb.getKpForTrainingData('training','orb')
orb.getKpForTestData('test-orb','test-orb')

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

def readTestData(name) :
    name = name + '.txt'
    with open(name) as f:
        for line in f:
            innerList = [float(elt.strip()) for elt in line.split(',')]
            testData.append(innerList)
readTestData('test-orb')

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

filledImages = readTrainingData('orb')
for index in filledImages:
    image = cv2.imread('training/' + fileList[index] + '.jpg') 
    cv2.imshow('image',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#chạy tất cả các ảnh trong csdl -> tìm 5 ảnh gần nhất.
#số ảnh đúng trong 5 ảnh là n  là n => tỉ lệ sẽ là n/5
#tỉ lệ chính xác sẽ bằng tổng số tỷ lệ / tổng số ảnh
#phương pháp nào có tỉ lệ cao nhất