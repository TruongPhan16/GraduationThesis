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

def readTrainingData(p):
    path = p + '/*.txt'
    files = glob.glob(path)
    tmp = []
    for name in files:
        with open(name) as f:
            for line in f:
                innerList = [float(elt.strip()) for elt in line.split(',')]
                trainingData.append(innerList)

readTrainingData('sift')
def readTestData(name) :
    name = name + '.txt'
    with open(name) as f:
        for line in f:
            innerList = [float(elt.strip()) for elt in line.split(',')]
            testData.append(innerList)
readTestData('test')
def euclidean(vector1, vector2):
    dist = [(a - b)**2 for a, b in zip(np.array(vector1), np.array(vector2))]
    dist = math.sqrt(sum(dist))
    return dist
    
# maxDistance = 0
# maxCount = 0
# m = 400
# indexResult = 0
# dataCount = []
# result = []
# count = 0
# for i in testData:
#     minDis = 0
#     for j in trainingData:
#         distant = euclidean(i,j)
#         if (minDis == 0):
#             minDis = distant
#         else:
#             if (distant < minDis):
#                 minDis = distant
#     if(minDis < m):
#         count = count + 1
# dataCount.append(count)
# if(count > maxCount):
#     maxCount = count
# for j in dataCount:
#     if (j == maxCount):
#         result.append(dataCount.index(j))
# print result

def findDistance(v1, v2, t):
    distance = []
    minDistance = 0
    for i in v1:
        for j in v2:
            dist.append(euclidean(i,j))
            # dist = euclidean(i,j)
            # distance.append(dist)
    print dist
    # minDistance = min(float(s) for s in dist)
    # print distance             
findDistance(test1, test2,400)